# coding: utf-8

import numpy as np
import random
import math
import nltk
from scipy.special import gamma, gammaln
from nltk.corpus import stopwords
import sys
import re

stopset = set(stopwords.words('english'))

wre = re.compile (r"(\w)+")

def get_words(text):
    l = 0
    while 1 < len(text):
        s = wre.search(text, l)
        try:
            yield text[s.start():s.end()]
            l = s.end()
        except:
            break

def category (probs):
    return np.argmax(np.random.multinomial(1, probs))

def mean(x):
    return sum(x)/len(x)

def gamma_pdf(x, k, theta):
    x, k, theta = map(float, (x, k, theta))
    return (x**(k-1))*(math.exp(-x/theta))/((theta**k)*gamma(k))

def exp_pdf(x, k):
    return k*math.exp(-k*x)

class LDASampler(object):
    def __init__(self):
        self.all_words = []
        self.reverse_map = {}
        self.documents =[]
        self.Ndocuments = 0
        self.Nwords = 0
        self.alpha = 1.0 # alpha = 0.1, 0.5, 1.0
        self.beta = 1.0  # beta = 0.1, 0.5, 1.0

    def load_as_bag(self, document):    # Creates a bag of words for a single document"
        v = []
        for w in get_words(document):
            w = w.lower()
            if not w in stopset:   # Remove stopwords
                if not w in self.reverse_map:
                    self.reverse_map[w] = self.Nwords
                    self.all_words.append(w)
                    self.Nwords += 1
                v.append(self.reverse_map[w])
        self.documents.append(v)

    def cond_dist(self, d, i, w):   # Define conditional probability
        to = self.assignments[d][i]
        self.Nwtcs[to] -= 1
        self.Ntdcs[d] -= 1
        self.Nwt[w,to] -= 1         # Number of times topic assigned to word
        self.Ntd[d,to] -= 1         # Number of tokens with topic in document
        aa = (self.Nwt [w] + self.beta)
        bb = (self.Nwtcs + self.pb)
        cc = (self.Ntd[d] + self.alpha)
        dd = (self.Ntdcs[d] + self.pa)
        pt = (aa/bb)*(cc/dd)
        pt /= np.sum(pt)
        nt = category(pt)
        self.assignments[d][i] = nt
        self.Nwtcs[nt] += 1
        self.Ntdcs[d] += 1
        self.Nwt[w, nt] += 1
        self.Ntd [d, nt] += 1
        return pt[nt]

    def phi_theta(self):            # Define phi and theta
        phi = self.beta*np.ones((self.Ntopics, self.Nwords))
        theta = self.alpha*np.ones((self.Ndocuments, self.Ntopics))
        for d in xrange(self.Ndocuments):
            for i,w in enumerate(self.documents[d]):
                t = self.assignments[d][i]
                phi[t, w] += 1
                theta[d, t] += 1
        return phi, theta
    
    
    def likelihood(self):           # Computes the likelihood of the parameters
        f1 = self.Ndocuments*(gammaln(self.Ntopics*self.alpha) - self.Ntopics*gammaln(self.alpha))
        f1 += np.log(gamma_pdf(self.alpha, 0.1, 1))
        f1 += np.log(gamma_pdf(self.beta, 0.1, 1))
        vt = np.zeros(self.Ntopics)
        f2 = 0
        for d in xrange(self.Ndocuments):
            vt.fill(0)
            for i, w in enumerate(self.documents[d]):
                vt[self.assignments[d][i]] += 1
            vt += self.alpha
            f2t1 = np.sum(gammaln(vt))
            f2t2 = gammaln(self.Ntdcs[d] + self.Ntopics*self.alpha)
            f2 += f2t1 - f2t2
        return f1 + f2

    def initialize(self):           # Initialization of LDA
        for d in xrange(self.Ndocuments):
            for i, w in enumerate(self.documents[d]):
                z = random.randint(0, self.Ntopics - 1)
                self.assignments [d][i] = z
                self.Nwt[w,z] += 1
                self.Ntd[d,z] += 1
                self.Nwtcs[z] += 1
                self.Ntdcs[d] += 1
        self.pa = self.alpha*self.Nwords
        self.pb = self.beta*self.Ntopics

    def iterate(self):
        for document in xrange(self.Ndocuments):
            for i, word in enumerate(self.documents[document]):
                pp = self.cond_dist(document, i, word)
    
        
    def resample_alpha(self, lik):
        oldalpha = self.alpha
        self.alpha = np.random.exponential(self.alpha)
        self.pa = self.alpha*self.Nwords
        self.pb = self.beta*self.Ntopics
        nlik = self.likelihood()
        pratio = np.exp(nlik - lik)
        qratio = exp_pdf(self.alpha, oldalpha) / exp_pdf(oldalpha, self.alpha)
        if random.random() < pratio*qratio:
            return nlik
        self.alpha = oldalpha
        self.pa = self.alpha*self.Nwords
        self.pb = self.beta*self.Ntopics
        return lik

    def resample_beta(self, lik):
        oldbeta = self.beta
        self.beta = np.random.exponential(self.beta)
        self.pa = self.alpha*self.Nwords
        self.pb = self.beta*self.Ntopics
        nlik = self.likelihood()
        pratio = np.exp(nlik - lik)
        qratio = exp_pdf(self.beta, oldbeta) / exp_pdf(oldbeta, self.beta)
        if random.random() < pratio*qratio:
            return nlik
        self.beta = oldbeta
        self.pa = self.alpha*self.Nwords
        self.pb = self.beta*self.Ntopics
        return lik

    def run(self, Ntopics, burnin, interval, nsamples):
        self.Ntopics = Ntopics
        self.Nwords = len(self.all_words)
        self.Ndocuments = len(self.documents)
        self.assignments = [[0 for w in d] for d in self.documents]
        self.Nwt = np.zeros((self.Nwords, self.Ntopics))
        self.Ntd = np.zeros((self.Ndocuments, self.Ntopics))
        self.Nwtcs = np.zeros(self.Ntopics)
        self.Ntdcs = np.zeros(self.Ndocuments)
        old_lik = -np.inf
        samples = []
        self.initialize()
        iteration = 0
        while len(samples) < nsamples:
            iteration += 1
            self.iterate()
            lik = self.likelihood()
            lik = self.resample_alpha(lik)
            lik = self.resample_beta(lik)
            print(self.alpha, self.beta, lik)
            self.print_topic_proportions()
            print(lik)
            if iteration > burnin and iteration % interval == 0:
                samples.append(self.phi_theta())
        return mean([a[0] for a in samples]), mean([a[1] for a in samples])

    def print_topic_proportions(self):
        tcounts = np.zeros(self.Ntopics)
        for d in xrange(self.Ndocuments):
            for w in self.assignments[d]:
                tcounts[w] += 1
        tcounts /= sum(tcounts)
        for t in tcounts:
            print("%.3f"%t,)
        print

    def print_topic(self, phi, t, n):
        print ("topic", t, ":")
        s = np.argsort(-phi[t])
        for w in s[:n]:
            print( "     ", self.all_words[w])

    def print_topics(self, phi, n):
        for t in xrange(len(phi)):
            self.print_topic(phi, t, n)
            print

    def make_reverse_map(self):
        for i, w in enumerate(self.all_words):
            self.reverse_map[w] = i

    def parse_lda_data(self, prefix):
        data_f = file(prefix+ ".data")
        vocab = [a.strip() for a in file(prefix+ ".vocab")]
        self.all_words= vocab
        self.make_reverse_map()
        self.Nwords = len(vocab)
        data = [a.strip().split() for a in data_f]
        self.Ndocuments = len(data)
        self.documents = [[] for i in xrange(self.Ndocuments)]
        for doc in xrange(self.Ndocuments):
            for word in data[doc][1:]:
                w, c = map(int, word.split(";"))
                if w >= len(self.all_words):
                    print(w, c)
                    w = len(all_words) - 1
                [self.documents[doc].append(w) for i in xrange(c)]

f = ("movie2.txt")

if __name__ =='__main__':
    s = LDASampler()
    [s.load_as_bag(x) for x in file(f).read().split("\r\n\r\n")]
    phi, theta = s.run(10, 1., 1., 9)
    print("returned")
    s.print_topics(phi, 10)




            






        
    


        


        



    
