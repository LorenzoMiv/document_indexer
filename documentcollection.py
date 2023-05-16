from typing import List
import vectorizerwrapper
import document

class DocumentCollection:
    def __init__(self, documents: List[str], vectorizer: vectorizerwrapper.TfidfVectorizerWrapper):
        self.vectorizer = vectorizer
        #create a matrix of tf_idf scores where rows are documents and collumns are terms
        #It would be a better implementation to throw this matrix out after the documents are generated
        #for now I'm keeping it since there may be additional operations to perform on the matrix
        self.tfidf_matrix = self.vectorizer.fit_transform(documents)
        self.documents = self.add_documents(len(documents))

    def add_documents(self, document_count):
        #eventually this should use get_feature_names_out instead of inverse_transform
        #do not currently know how to identify the source document with get_feature_names_out
        term_lists = self.vectorizer.inverse_transform(self.tfidf_matrix)
        documents = []
        for i in range(document_count):
            tfidf_scores = self.tfidf_matrix[i]
            doc_terms = term_lists[i]
            documents.append(document.Document(doc_terms, tfidf_scores))
        return documents
            