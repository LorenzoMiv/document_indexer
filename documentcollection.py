from typing import List
import vectorizerwrapper

class DocumentCollection:
    def __init__(self, documents: List[str], TfidfVectorizer: vectorizerwrapper.TfidfVectorizerWrapper):
        self.documents = documents
        self.vectorizer = TfidfVectorizer
        #create a matrix of tf_idf scores for each term in each document
        self.tf_idf_matrix = self.vectorizer.fit_transform([d.terms for d in documents])

    def preprocess(self):
        #perform tokenization, lowercasing, stop word removal,
        #and various other preprocessing on document strings
        pass
