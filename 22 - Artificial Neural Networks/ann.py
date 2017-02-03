# Artificial Neural Network

# Installing Theano to exploit parallel computations of processor
# install from command prompt as admin
#(open from spyder using Tools>Open Command Prompt but I found I needed to open prompt from OS to do as admin) 
# (if you get a permission error try closing python as ith might be files are in use)
# using following command
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Install Tensorflow as will be used by Keras - again run commands as admin
# Install Tensorflow from the website: https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html
# the CPU version will be fine for this exercise
# we are using anaconda and python 3.5 so will want the Anaconda Installation option
# on windows I ran "conda create -n tensorflow python=3.5"
# and "pip install --upgrade https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow-0.12.1-cp35-cp35m-win_amd64.whl --ignore-installed"
# needed to have anaconda closed when running this

# Installing Keras, which will make use of Tensorflow
# pip install --upgrade keras

# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
#we skip first few columns as they are just identifiers that have no impact on y variable
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

# Encoding categorical data
# columns index 1 and 2 are country and gender
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
#only need to do onehotencoding if more than two values so just country and not gender
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
#and we remove one of the columns the onehotencoding because it can be derived (avoiding the dummy variable trap)
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Part 2 - Now let's make the ANN!

# Importing the Keras libraries and packages
# Seqeuntial for initialising and Dense for adding layers
from keras.models import Sequential
from keras.layers import Dense

# Initialising the ANN
# we're going to use two hidden layers
classifier = Sequential()

# Adding the input layer and the first hidden layer
#input_dim is 11 because we have 11 independent variables so 11 nodes in input layer
#using the rectifier activation function (relu)
#6 nodes in first hidden layer
#arrived at as mean of nodes in input layer and output layer
#initi is the initialisation of the weights - uniform gives a uniform distribution of values near 0
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu', input_dim = 11))

# Adding the second hidden layer
#may not actually need a second hidden layer for this example but it illustrates idea
#no need to specify input_dim as it's now implicit from previous layer's output
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu'))

# Adding the output layer
# sigmoid preferred for output layer as sigmoid gives probability outputs (probability of leaving bank)
# only one output node because our outcome is one binary variable
# if we had multiple classes for outcome then we'd use multiple nodes and softmax activation
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
# using the adam variant of stochastic gradient descent
# loss or error function is chosen as binary_crossentropy, which is logarithmic loss function for sigmoid
# if we had multiple outcomes then we would use categorical_crossentropy instead
# optimising model for accurancy, though metrics parameter can take list
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
# this is stochastic gradient descent so set batch size, here 10
# limit number of epochs to 100
classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 100)

# Part 3 - Making the predictions and evaluating the model

# Predicting the Test set results
# outcomes are probabilities so need to conver to True/False to make confusion matrix
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)