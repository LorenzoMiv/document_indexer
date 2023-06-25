#goal:  evaluate a given string and access the cosine similarity of the string. 
#       we wish to discern which table should be pulled due to the cosine similarity score from the string
#       approach: take in a string, break the string up into pieces, 
'''
    steps:
    1. preprocess and vectorize the query
    2. filter the documents based on the inverted index. Return only those that have a word in common with the query
    3. compare each return document's tf-idf vector with the query's tf-idf vector to calculate the cosine similarity.
    4. rank each document based on the cosine similarity
'''
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

#function that will split a string into an array and vectorize the query
documents = ["Document 1 - this is document 1", "Doc 2: Machine Learning and AI Practices", "Document 3:This is Data Visualiztion"]
#declare some count vectorizer to use
vectorizer = CountVectorizer()
#convert the words in the docs to lowercase 
for words in documents:
    words.lower()
''' 
    assigns an index to each word
    there are 10 different words in the document so we have a total of ten elements and three docs in the example
    meaning we have a 3X10
'''
vectorizer.fit(documents)
#test: displays the words and their associated element position
print("Vocabulary: ", vectorizer.vocabulary_)
#vectorize the doc, creates an array and tracks the amount of terms used in relation to the set of words
vectorize_doc = vectorizer.transform(documents)

print(vectorize_doc.toarray())
def string_parser(input_string):
    
    ps = PorterStemmer()

    #tokenize data 
    tokenize_string = word_tokenize(input_string)
    
    #new string for data
    stem_token_string = []
    
    #stem tokenized words
    for word in tokenize_string:
        stem_token_string.append(ps.stem(word))


    return tokenize_string


#testing    
a_string = "This is a test query."
print(string_parser(a_string))
