# Apriori

# Data Preprocessing
# install.packages('arules')
library(arules)
dataset = read.csv('Market_Basket_Optimisation.csv', header = FALSE)
#we're removing duplicates as they are taken to be mistakes
#the read.transactions function is able to deal with blanks - it handles as sparse matrix
#it captures the data in the form needed to be able to train a model
dataset = read.transactions('Market_Basket_Optimisation.csv', sep = ',', rm.duplicates = TRUE)
#interactively inspect data set
summary(dataset)
itemFrequencyPlot(dataset, topN = 10)

# Training Apriori on the dataset
# taking minimum support to be items purchased at least 4 times a day (so 7*4 / 7501 )
# this is number of transactions with those products as proportion of total - approximately 0.004
# to set confidence we actually start with default (0.8) and then play with it until we get useful rules
# the default gives no rules at all, since no rules obtain in 80% of transactions
# instead we settle on a lower confidence of 0.2
rules = apriori(data = dataset, parameter = list(support = 0.004, confidence = 0.2))

# Visualising the results
#this shows 10 strongest rules
inspect(sort(rules, by = 'lift')[1:10])