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
        #print(self.vectorizer)
        #print(self.vectorizer.get_feature_names())
        #print(self.tfidf_matrix)
        self.documents = self.add_documents()

    def add_documents(self):
        document_dict = {}
        term_lib = self.vectorizer.get_feature_names()
        #shape returns the number of rows in the matrix
        for row_num in range(self.tfidf_matrix.get_shape()[0]):
            term_scores = []
            #isolate the row
            row  = self.tfidf_matrix.getrow(row_num)
            #nonzero gets the column numbers of terms contained in each doc
            for col in row.nonzero()[1]:
                term_scores.append((term_lib[col], self.tfidf_matrix[row_num, col]))
            #eventually this code should be changed so that adding a document
            #takes the next available place in the dictionary
            document_dict[row_num] = document.Document(row_num, term_scores)
        return document_dict