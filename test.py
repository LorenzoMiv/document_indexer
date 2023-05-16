import documentcollection
import vectorizerwrapper
import document

def test_document_collection(collection: documentcollection.DocumentCollection):
    for doc in collection.documents:
        collection.documents[doc].display()

print("starting program\n")
document1 = "The quick brown fox jumps over the lazy dog."
document2 = "The cat and the hat."
document3 = "A brown cat and a black dog."
doc_list = [document1, document2, document3]
vect = vectorizerwrapper.TfidfVectorizerWrapper()
collection = documentcollection.DocumentCollection(doc_list, vect)
test_document_collection(collection)