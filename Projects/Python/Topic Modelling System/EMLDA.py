#-*- coding: utf-8 -*-

import nltk
import pickle
import numpy as np
import gensim
from gensim import corpora, models
from stop_words import get_stop_words

# Open file
raw = open("/Users/Robin/Desktop/Computational Linguistics/Chapter 8 LDA/movie2.txt").read()
content = unicode(raw, errors='ignore')

# Sentence Segmentation
segmenter_file = open('english.pickle', 'r')
sentence_segmenter = pickle.Unpickler(segmenter_file).load()
texts = sentence_segmenter.tokenize(content)

# Remove punctuations from document
stopwords = get_stop_words('english')
punctuations = ['(', ')', ':', ';', ',', '-', '!', '.', '?', '/', '"', '--', '*']
filtered = [[word for word in text.lower().split() if word not in punctuations]
         for text in texts]

# Remove English stopwords from document
stopwords = get_stop_words('english')
documents = [[word for word in f if word not in stopwords]
         for f in filtered]

# Create dictionary and corpus
dictionary = corpora.Dictionary(documents)
corpus = [dictionary.doc2bow(document) for document in documents]

# Print out top 10 most probable topics for LDA
lda = gensim.models.ldamodel.LdaModel(corpus, id2word = dictionary, num_topics = 10)

for top in lda.print_topics(10):
    print top


