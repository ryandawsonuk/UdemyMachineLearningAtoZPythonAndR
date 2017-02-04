#Linear Regression

Simple case study in linear regression. Dataset has just two variables - years of experience and salary. We fit a linear model using the training data and check it against the test data.

So dependent variable y is salary and only independent variable x is years of experience. The assumption is of a relationship of the form y = constant + coefficient*x. So the model training aims to set value for constant and coefficient. In this example this is done using library functions (which minimise the distance between the fit line and the training datapoints - ordinary least squares) and the resulting model is then visualised.