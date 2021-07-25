from preprocessor import Preprocessor
from labelEncoder import LabelEncoder
from logisticRegression import LogisticRegression 
from bayesClassifier import BayesClassifier
from confusionMatrix import Confusion

class Main:
    def preprocessor(self):
        preprocess = Preprocessor()
        preprocess.binarize()
        preprocess.mean()
        preprocess.scaling()
        preprocess.normalize()

    def encoder(self):
        encoder = LabelEncoder()
        encoder.encoder()
        encoder.decoder()

    def logistic(self):
        classifier = LogisticRegression()
        classifier.logistic()

    def bayesClassifier(self):
        classifier = BayesClassifier() 
        classifier.classifier()
        classifier.newClassifier()

    def confusionMatrix(self):
        confusion = Confusion()
        confusion.matrix()

if __name__ == "__main__":        
    main = Main()
    #main.preprocessor()
    #main.encoder()
    #main.logistic()
    #main.bayesClassifier()
    main.confusionMatrix()

