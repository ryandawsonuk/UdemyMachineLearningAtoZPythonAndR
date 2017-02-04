# Logistic Regression

Logistic regression differs from linear regression in that

* The logistic regression model is typically used to derive a probability and then that probability is translated into an expected outcome category. This is what makes it a classifier.
* The trend curve that models likelihood of outcomes is a sigmoid function rather than a linear function.

Logistic regression gets its name from the outcome being either zero or one, though the approach can be extended to classify under multiple outcomes using a One Vs All or One Vs Rest approach. (This means deriving the probability of each outcome for a datapoint and taking the highest.)

The data for this example represents social media users. Each row contains a User ID, Gender, Age, Estimated Salary and whether or not the user Purchased an item in response to an advert (e.g. a car advert). Only the Age and EstimatedSalary will be used as features. The trained model will predict whether a user is likely to make a purchase based on an advert. 

The template files are not part of the example and just show that there are general patterns across classifiers.

The example also shows how to visualise the output.