# Artificial Neural Network

# Importing the dataset
#we skip first few columns as they are just identifiers that have no impact on y variable
dataset = read.csv('Churn_Modelling.csv')
dataset = dataset[4:14]

# Encoding the categorical variables as factors
dataset$Geography = as.numeric(factor(dataset$Geography,
                                      levels = c('France', 'Spain', 'Germany'),
                                      labels = c(1, 2, 3)))
dataset$Gender = as.numeric(factor(dataset$Gender,
                                   levels = c('Female', 'Male'),
                                   labels = c(1, 2)))

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Exited, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
training_set[-11] = scale(training_set[-11])
test_set[-11] = scale(test_set[-11])

# Fitting ANN to the Training set
# install.packages('h2o')
# using h2o over pluralnet, nnet or deepnet
# pluralnet would only do regressors and we need classifier and nnet only support 1 hidden layer
# h20 is open source and can use parallelism and supports convenient parameter tuning
library(h2o)
# unlimited threads/cores
h2o.init(nthreads = -1)

#as.h2o converts the data set into an h2o data frame
#2 hidden layers, 6 nodes in each hidden layer (6 is based on average of nodes in input and output layers)
#h2o knows number of input and output nodes because we told it y and training_frame
#the -2 value for train_samples_per_iteration means auto-tune batch size
classifier = h2o.deeplearning(y = 'Exited',
                              training_frame = as.h2o(training_set),
                              activation = 'Rectifier',
                              hidden = c(6,6),
                              epochs = 100,
                              train_samples_per_iteration = -2)

# Predicting the Test set results
prob_pred = h2o.predict(classifier, newdata = as.h2o(test_set[-11]))
y_pred = (prob_pred > 0.5)
y_pred = as.vector(y_pred)

# Making the Confusion Matrix
cm = table(test_set[, 11], y_pred)

# h2o.shutdown()