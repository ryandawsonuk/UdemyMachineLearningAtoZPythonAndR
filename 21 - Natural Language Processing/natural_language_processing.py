# Natural Language Processing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
#quoting=3 means ignore double-quotes
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

# Cleaning the texts
import re
import nltk
#we want to download stopwords from nltk as we use it to remove non-relevant words
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
#corpus is the list of all cleaned reviews
corpus = []
#run through each review and clean
for i in range(0, 1000):
	#remove any punctuation or numbers and substitute with spaces - just keep letters
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
	#make all letters lowercase
    review = review.lower()
	#turn review into a split out list of words rather than one big string
    review = review.split()
	#remove the words like connector words using stopwords - i.e. trim to only words not in english stopwords
	#at the same time we apply stemming to shorten words like 'loved' down to root 'love'
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
	# join the list back into a single string, sepearated by spaces
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
# each distinct word is transformed into a column and given a numeric value for number of occurrences in a review
# actually a sparse matrix as most columns would be zero
# CountVectorizer is designed to extract words and transform their counts into features in a sparse matrix
# setting max_features so that most words (1565 total) are kept but some of the least-frequent words get cut
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
# now we have feature matrix, also need target variable
# can just take this from column of original dataset as it is in the same row ordering as feature matrix
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)