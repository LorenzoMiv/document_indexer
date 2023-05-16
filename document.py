class Document:
    
    def __init__(self, doc_id, term_scores):
        self.doc_id = doc_id
        self.term_scores = term_scores

    def display(self):
        print("doc:", self.doc_id, "\nterms:\n", self.term_scores)