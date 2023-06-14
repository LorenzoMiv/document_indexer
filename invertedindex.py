from collections import defaultdict

class InvertedIndex:

#create sparse inverted index of documents
    def __init__(self, documents):
        self.matrix = self.add_documents(documents)
        
    
        
    def add_documents(self, documents):
        matrix = defaultdict(set)
        for doc in documents:
            for term in documents[doc].term_scores:
                matrix[term[0]].add((documents[doc].doc_id, term[1]))
        #print(self.inverted_index)
        return matrix
    
    def display(self):
        terms = self.matrix.keys()
        for term in terms:
            print("term:", term)
            print("document id and score:")
            print(self.matrix[term])
            