# Multiple Linear Regression

# Importing the dataset
dataset = read.csv('50_Startups.csv')
# dataset = dataset[, 2:3]

# Encoding categorical data by factorising State variable
dataset$State = factor(dataset$State,
                       levels = c('New York', 'California', 'Florida'),
                       labels = c(1, 2, 3))

# Splitting the dataset into the Training set and Test set
# Use 80% of data as training set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# No Feature Scaling as lm takes care of it
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])

# Fitting Multiple Linear Regression to the Training set
# The dot in the formula means all of the indendent variables (the variables other than Profit)
regressor = lm(formula = Profit ~ .,
               data = training_set)

# Predicting the Test set results
y_pred = predict(regressor, newdata = test_set)

# Building the optimal model using Backward Elimination
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
               data = dataset)
#check p-values of variables as variable with hightest p-value can be eliminated
summary(regressor)
# Optional Step: Remove State2 only (as opposed to removing State directly)
# regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + factor(State, exclude = 2),
#                data = dataset)
# summary(regressor)
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend,
               data = dataset)
#choosing variable with highest p-value by interactively inspecting summary from regressor
summary(regressor)
regressor = lm(formula = Profit ~ R.D.Spend + Marketing.Spend,
               data = dataset)
summary(regressor)
#significance level taken to be 5% - optimised model has p-values for each variable lower than this
regressor = lm(formula = Profit ~ R.D.Spend,
               data = dataset)
summary(regressor)