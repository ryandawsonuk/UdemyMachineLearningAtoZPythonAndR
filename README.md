# Machine Learning A-Z

These are my notes from the course Machine Learning A-Z. Many of the code files are provided in the course and reproduced here - I've modified and added my own narrative to help me return to the content more easily. I've also changed the numbering of topics a bit for the same reason. Code comments I've added are more detailed on the first instance of a technique and so later examples are less heavily commented if they make use of techniques already previously introduced.

The examples are deliberately each quite small and don't use much in the way of Class structure or even functions as the purpose is just focus on each specific method.

Note that it is assumed throughout that the working directory is set as the directory containing any files to process.

## 1 Data Preprocessing

Uses a data set which contains records of customers and whether they bought a product or not. Features are country, age and salary. Covers:

* Test-train split of data set.
* Imputing missing values.
* Handling categorical data.
* Feature scaling.

## 2 Simple Linear Regression

Uses a data set of YearsOfExperience and Salary and fits a linear model.

## 3 Multiple Linear Regression

Example of multiple linear regression - fitting linear model with multiple variables. Uses data set of startups using variables R&D Spend, Administration, Marketing Spend, State and Profit. Covers:

* Use of linear regression library
* Avoiding dummy variable trap by removing redundant column on dummied categorical variable
* Backward elimination of features which have least correlation (highest p-value)

## 4 Polynomial Regression

Uses a data set of Level and Salary. The example illustrates how polynomial linear regression is just like linear regression except that we create derived polynomial features by raising the base features to successively higher powers.

## 5 Support Vector Regression

Illustrates SVM regression with a non-linear kernel in relation to the Level and Salary data set.

## 6 Decision Tree Regression

Explanation of principle behind decision tree regression and illustration as applied to the Level and Salary data set.

## 7 Random Forest Regression

Much like previous regression examples, same data but this time random forest.

## Interlude on Evaluating Models

No examples for the interlude so no directory included but the course takes a break after regression models to explain concepts about evaluating model performance. It explains that R squared is a measure of the sum of the squared residuals (errors) relative to the same measure for a trendline that simply takes an average. R squared is 1 - the squared errors of the model divided by the squared errors of an average-line. So it tends to 1 as errors tend to zero. 

It also explains that adjusted R squared is a better judge of the model since it is a measure which penalises a model for having lots of variables.

The course then moves on to classifiers as evaluating models is a topic that is to be returned to later.

## 8 Logistic Regression

The example represents social media users. Each row contains a User ID, Gender, Age, Estimated Salary and whether or not the user Purchased an item in response to an advert (e.g. a car advert). Only the Age and EstimatedSalary will be used as features. The trained model will predict whether a user is likely to make a purchase based on an advert. 

The example includes some explanation of logistic regression and illustrates how to create a plot that can be used to evaluate the classifier. The same plotting approach is re-used for subsequent classifier examples but the detailed comments on how it works are in this example.

## 9 K-Nearest Neighbours (KNN) Classification

Example of a KNN classifier with explanation of the principles behind the example.

## 10 Support Vector Machine (SVM)

Example of SVM classification with linear decision boundary.

## 11 Kernel SVM

Example of SVM with non-linear decision boundary using a Kernel.

## 12 Naive Bayes

Example of Naive Bayes for classification.

## 13 Decision Trees for Classification

Example of decision tree for classification. A previous example showed decision tree regression. That was used to predict values along a line by breaking the line into blocks. For classification the blocks are instead drawn over the data to form groupings.

## 14 Random Forest for Classification

Much as with decision trees, we've previously seen an example of random forest for regression. This shows an example for classification.

Also included is a comparison of different classifiers.

## 15 K-means Clustering

With clustering we want to break data into groups but we don't have any information on correct categories. We're just looking for likeness.

This example illustrates clustering with K-means.

## 16 Hierarchical Clustering

Clustering by repeatedly forming clusters until there's only one and then choosing number of clusters by working back off the data recorded in a dendrogram. Also included is a comparison of different clustering techniques.

## 17 A Priori Association Rule Learning

Example for learning association rules and inspecting results. The example is a market basket situation based upon a store in the south of France.

## 18 Eclat for Association Rules

This example just gives a way of seeing items most frequently purchased together.

## 19 Upper Confidence Bound Reinforcement Learning

Example of reinforcement learning to maximise click-through rate on advert selection. Uses dummy data file to mock user selections. 

## 20 Thompson Sampling Reinforcement Learning

Thompson sampling applied to the same problem as the UCB example.
