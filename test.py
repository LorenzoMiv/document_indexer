import documentcollection
import vectorizerwrapper
import invertedindex
import lsh_index
import mongoDBconnection

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
#lsh = lsh_index.LSHindex(collection, 0.5)

# Mongodb connection test
connectionString = 'mongodb+srv://aXs35Ah10vEFCiaX:aXs35Ah10vEFCiaX@cluster0.niqlshf.mongodb.net/?retryWrites=true&w=majority'
retriever = mongoDBconnection.MongoDBPayloadRetriever(connectionString, 'test')
sensor_data = retriever.retrieve_payloads()
#for sensor_name, values in sensor_data.items():
#    print(sensor_name, values , "\n\n")

#create a list of sensor names and all of the data points associated with them
#sensor data also have a timestamp and topic field that are not accessed here
sensor_list = []
for sensor_name in sensor_data:
    sensor_list.append(sensor_name)

print("showing the list of sensor names: ")
print(sensor_list, '\n\n')

#create a new document collection containing the sensor names
sensor_collection = documentcollection.DocumentCollection(sensor_list, vect)
print("showing collection:")
test_document_collection(sensor_collection)

#create an inverted index of the sensor names and calculating tf-idf for each word in the name
sensor_inv_index = invertedindex.InvertedIndex(sensor_collection.documents)
print("\nshowing inverted index:")
sensor_inv_index.display()

#simple demo query that finds the document with the highest score for any query term
print("type a query term")
term  = input()
#print(sensor_inv_index.matrix.get(term))
high_score = 0
best_doc = -1
for document in sensor_inv_index.matrix.get(term):
    if document[1] > high_score:
        best_doc = document[0]
if best_doc == -1:
    print("not a term in the index")
else:
    print('\n', sensor_list[best_doc], '\n', sensor_data.get(sensor_list[best_doc]))

#cosine similarity query
print("\n\ntype several terms and get the most relevant query")
