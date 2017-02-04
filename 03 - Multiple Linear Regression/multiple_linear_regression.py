# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
#data set of startups using variables R&D Spend, Administration, Marketing Spend, State and Profit
dataset = pd.read_csv('50_Startups.csv')
#independent variables are all columns but last
X = dataset.iloc[:, :-1].values
#dependent variable is last (profit)
y = dataset.iloc[:, 4].values

# Encoding categorical data (state - column index 3)
# transforms categorical entries to 1-0 columns (LabelEncoder to numbers then OneHotEncoder to columns)
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
# one of the dummy variables is implied by others so remove one(any one will do)
#dummy columns put at beginning by encoder
#1: takes all columns inc index 1 (i.e. all but 0)
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
# Use 80% of data as training set and 20% as test
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# No Feature Scaling LinearRegression class takes care of it
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
#these can then be manually inspected in IDE's explorer by correlating with y_test (rows are in same order)
#script doesn't do the comparison
y_pred = regressor.predict(X_test)

# Building the optimal model using Backward Elimination
# eliminate variables that are not stastically significant
import statsmodels.formula.api as sm
#statsmodels wants a constant term in the model but all of columns in X are currently variables
#so put an integer 1 (any constant will do) in all 50 rows for this new column (added vertically - axis has to be specified)
#actually strictly we're using append to add X to the column of 1s and then assign the result back to X
X = np.append(arr = np.ones((50, 1)).astype(int), values = X, axis = 1)
#going to filter X_opt down to the optimal set of features - start with all of them
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
#create an Ordinary Least Squares implementation of the model using OLS (passing in feature data set and target data set)
#need this other implementation in order to find the highest p-values for pruning
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
#summary shows p-values
regressor_OLS.summary()
#manual inspection of summary data shows that column 2 should be removed
X_opt = X[:, [0, 1, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()
#repeat getting summary p-value data, manually inspect and remove hightest p-value column - this time 1
X_opt = X[:, [0, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()
X_opt = X[:, [0, 3, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()
#column 5 also has a p-value of more than 5% (taken as significance level) so eliminating that too 
#variables remaining in optimised model then have p-values below 5%
#column 3 is R.D.Spend. (Column 0 is actually just the constant 1s column we had to add.)
X_opt = X[:, [0, 3]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()