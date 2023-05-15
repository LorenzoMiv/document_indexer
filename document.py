class Document:
    serialId = 0
    
    def __init__(self, terms, tf_idf):
        self.doc_id = Document.serialId
        Document.serialId += 1
        self.terms = terms
        self.tf_idf = tf_idf