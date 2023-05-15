from sklearn.feature_extraction.text import TfidfVectorizer

class TfidfVectorizerWrapper:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def fit_transform(self, documents):
        return self.vectorizer.fit_transform(documents)
    
    def get_feature_names(self):
        return self.vectorizer.get_feature_names_out()
    
    def inverse_transform(self, tfidf_matrix):
        self.vectorizer.inverse_transform(tfidf_matrix)