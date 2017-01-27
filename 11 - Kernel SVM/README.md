# Kernel SVM

As with previous SVM examples, the basic principle of an SVM is to take the points nearest to the decision boundary as 'support vectors' and try to maximise the distance between them and the boundary.

This time using a non-linear Kernel (Gaussian Radial Basis Function) to draw a non-linear decision boundary. The theory behind kernels is to allow the SVM to draw more complex decision boundaries by (in the background) creating derived features which let the SVM work on vectors in a higher-dimensional space (the actual decision boundary then ends up being in a space which cuts through this - we in effect project the space of the data into an extra dimension in order to create a curvature that a hyperplane can cut through).
