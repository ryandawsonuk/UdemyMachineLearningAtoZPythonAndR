# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
#The data set needs to be transformed to a list of lists
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, 7501):
	#our master list should contain a list for each row (there are 20 columns)
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

# Training Apriori on the dataset
# the apyori class is an implementation of the a priori algorithm taken from the python software foundation
# taking minimum support to be items purchased at least 3 times a day (so 7*3 / 7501 )
# this is number of transactions with those products as proportion of total - approximately 0.003
# to set confidence we actually start with default (0.8) and then play with it until we get useful rules
# the default gives no rules at all, since no rules obtain in 80% of transactions
# instead we settle on a lower confidence of 0.2
# min length is 2 as only want to consider transactions with at least 2 products
# filter by lift of at least 3 so we only get strong rules
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

# Visualising the results
# they should already be automatically sorted by the source library
results = list(rules)