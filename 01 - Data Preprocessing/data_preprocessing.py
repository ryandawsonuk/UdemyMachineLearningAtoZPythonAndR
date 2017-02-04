# Data Preprocessing Example

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
#:-1 means all columns except the last
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

#split test and train datasets - setting random_state acts as seed to ensure reproducibility
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=0)

#impute missing data, which will have 'NaN' values after import
#axis=0 means we are taking the mean across column
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy='mean', axis = 0)
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

#encoding categorical data
#column 0 in x is country and y captures whether purchased (yes-no)
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
x[:, 0] = labelencoder_x.fit_transform(x[:, 0])
#label encoding is enough for the yes-no column (the y column)
#but we need to employ dummy/one-hot encoding for country column (first column in x) 
onehotencoder = OneHotEncoder(categorical_features = [0])
x = onehotencoder.fit_transform(x).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#apply feature scaling to prevent salary feature from dominating the model
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.fit_transform(x_test)
#don't need to scale y as it's a classification problem (yes/no as 0/1)