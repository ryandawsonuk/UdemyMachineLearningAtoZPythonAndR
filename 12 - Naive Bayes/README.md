# Naive Bayes

The naive bayes classifier works on Bayes theorem,  P(A|B) = ( P(B|A) * P(A) ) / P(B)

This can be applied to categorise a new data point. B is then the fact of the data point having a given set of features and A is the probability of the data point belonging to a given class.

The probability of having given features is estimated by drawing a circle around the datapoint (of a pre-determined radius) and then the observations within that circle are taken to be similar and so the probability of having those features can be approximated by the proportion of datapoints of a class in that circle out of the total.

The class chosen is the one which has the highest probability (the One vs Rest approach).

It is called Naive Bayes because it assumes the variables are independent of one another, which often they are not. But it's still used because it can still give good results.

