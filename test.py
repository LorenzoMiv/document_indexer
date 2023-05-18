import documentcollection
import vectorizerwrapper
import invertedindex
import lsh_index

def test_document_collection(collection: documentcollection.DocumentCollection):
    for doc in collection.documents:
        collection.documents[doc].display()

print("\nstarting program...\n")
document1 = "The quick brown fox jumps over the lazy dog."
document2 = "The cat and the hat."
document3 = "A brown cat and a black dog."
doc_list = [document1, document2, document3]

#document collection
vect = vectorizerwrapper.TfidfVectorizerWrapper()
#parameter for filtering stop words
vect.set_params()
collection = documentcollection.DocumentCollection(doc_list, vect)
print("showing collection:")
test_document_collection(collection)

#inverted index
inv_index = invertedindex.InvertedIndex(collection.documents)
print("\nshowing inverted index:")
inv_index.display()

#LSH
lsh = lsh_index.LSHindex(collection, 0.5)

