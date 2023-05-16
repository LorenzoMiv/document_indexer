from collections import defaultdict
import document

class InvertedIndex:

#create sparse inverted index of documents
    def __init__(self, documents):
        self.inverted_index = self.add_documents(documents)
        
    
        
    def add_documents(self, documents):
        inverted_index = defaultdict(set)
        doc: document.Document
        for doc in documents:
            for term in doc.terms:
                inverted_index[term].add((doc.doc_id, doc.tf_idf))
        #print(self.inverted_index)
        return inverted_index