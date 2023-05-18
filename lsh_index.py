from datasketch import MinHash, MinHashLSH

class LSHindex:

    def __init__(self, document_collection, chosen_threshold):
        self.lsh = MinHashLSH(threshold=chosen_threshold)
        #self.doc_min_hashes = self.hash_docs(document_collection)
        self.hash_docs(document_collection)

    def hash_docs(self, document_collection):
        #hash each document using its TF-IDF vector, then group them into buckets
        minhash = MinHash(num_perm=128)
        for doc in document_collection.documents:
            for score in document_collection.documents[doc].term_scores:
                minhash.update(str(score[1]).encode("utf-8"))
            self.lsh.insert(doc, minhash)