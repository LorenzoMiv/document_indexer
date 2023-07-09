'''
    steps:
    1. preprocess and vectorize the query
    2. filter the documents based on the inverted index. Return only those that have a word in common with the query
    3. compare each return document's tf-idf vector with the query's tf-idf vector to calculate the cosine similarity.
    4. rank each document based on the cosine similarity
    
    tf-idf: 
    Term Frequency (tf): number of times each term appears in a doc divided by the total numof words in the doc
    Inverse Doc Frequency: log of the number of docs divided by the number of docs that contain the word
    Note: creates a matrix for docs * vocab
'''
import numpy as np
from numpy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import re

#function that will split a string into an array and vectorize the query
documents = ["Document 1 - this is document 1", "Doc 2: Machine Learning and AI Practices", "Document 3:This is Data Visualization"]
#declare some count vectorizer to use
vectorizer = TfidfVectorizer()
cvectorizer = CountVectorizer()
#convert the words in the docs to lowercase 
for words in documents:
    words.lower()
''' 
    assigns an index to each word
    there are 10 different words in the document so we have a total of ten elements and three docs in the example
    meaning we have a 3X10
'''
matrix = vectorizer.fit_transform(documents)
######TEST#####
#print(vectorizer.get_feature_names_out())
#test: displays the words and their associated element position
#print("Vocabulary: ", vectorizer.vocabulary_)
#vectorize the doc, creates an array and tracks the amount of terms used in relation to the set of words
#print(matrix.toarray())
###############

#print(vectorize_doc.toarray())
#function that accepts a query to vectorize
def query_parser(query):
    #tokenize data
    query_arr = [query]
    print(query_arr)
    query_vector = vectorizer.fit_transform(query_arr)
    return query_vector.toarray()

#test
query = "This is a document to search for."
#strip string of punctuation using regex
strip_query = re.sub(r'[^\w\s]', '', query)
#print(query_parser(strip_query))

A = np.array(query_parser(strip_query))
B = np.array(matrix.toarray())
#cosine = np.dot(B, A)/(norm(B, axis=1) *norm(A))
#might need to adjust the dimensions, like pad the smaller matrix 

print("query vectorized: ", A, "\ndocuments vectorized: ", B)
print("\nDimension of A: ",  A.shape, "\nDimension of B: ", B.shape)