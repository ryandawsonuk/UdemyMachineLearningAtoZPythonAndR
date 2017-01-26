# Support Vector Regression

Using same non-linear data set of Level and Salary as previous exercise.

This is an illustration of how to use an SVM for regression rather than an explanation of the theory but the basic principle of an SVM is to take the points nearest to the decision boundary as 'support vectors' and try to maximise the distance between them and the boundary.

The problem here is non-linear so using a non-linear Kernel (Gaussian Radial Basis Function). The theory behind kernels is to allow the SVM to draw more complex decision boundaries by (in the background) creating derived features which let the SVM work on vectors in a higher-dimensional space (the actual decision boundary then ends up being in a space which cuts through this).

