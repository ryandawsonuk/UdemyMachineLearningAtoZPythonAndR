# Principal Component Analysis (PCA)

##PCA 

PCA is a feature extraction technique. It is a way of transforming the data set so as to create a set of derived data that captures the degree of highest variation.

This is possible because some variables are likely to vary with one another (covary) and if so it will be unnecessary to include all of them.

The technique actually breaks the data into eigenvector and yields associated eigenvalues. The largest eigenvalues reflect the variables that capture the most variation.

So PCA can yield a transformed data set in which a small number of variables might be able to explain/correlate to a very high percentage of variation in the data. The model can then be run efficiently on that data set.

## This Example - A Classification Problem

This example uses a public Wine dataset. Each row represents a wine sample and each column one of its properties. The dependent variable in the original data set is the region of origin of the wine but for this exercise it has been renamed 'Customer_Segment'.

We can imagine that there has been a blind taste test across a range of customers for a wine business and now we're trying to construct a model that will tell us which customer segments will like a given wine.

Note that there are quite a lot of columns, too many to plot. So it's an opportunity to do dimensionality reduction. If we can get it down to two features then we could visualise the results. So we can use PCA to extract two features which explain as much of the variation as possible.

In this example we transform the data set and just work with that. In the real world we would want to transform data back again for particular predictions. In Python we would do this with inverse_transform.

The actual classification problem is handled through LogisticRegression in the Python version and SVM in the R version.