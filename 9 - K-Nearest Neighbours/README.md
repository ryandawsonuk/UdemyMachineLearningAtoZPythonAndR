# K-Nearest Neighbours (KNN) Classification

The idea with KNN is to decide for each datapoint which category it should fall under by comparing against the data points which are most like it. The number of data points to consider (k) for each new data point is decided in advance. The criteria of 'likeness' is a measure of distance, typically Euclidean distance. So the distance between two data points is the root of the sum of the squares of the differences between their features.

The data set for this example is the same as that used for Logistic Regression. The example represents social media users. Only the Age and EstimatedSalary will be used as features. The trained model will predict whether a user is likely to make a purchase based on an advert. 

The decision boundary for KNN is non-linear and for this example this allows it to give more accurate results than logistic regression.