from sklearn.feature_extraction.text import TfidfVectorizer

#view documentation here: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.inverse_transform
class TfidfVectorizerWrapper:
    #wrapper should help make sure there aren't more than one Vectorizer object
    #it also limits the available methods
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def fit_transform(self, documents):
        return self.vectorizer.fit_transform(documents)
    
    def get_feature_names(self):
        return self.vectorizer.get_feature_names_out()
    
    def inverse_transform(self, tfidf_matrix):
        self.vectorizer.inverse_transform(tfidf_matrix)