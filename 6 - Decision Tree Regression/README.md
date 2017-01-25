# Decision Tree Regression

The idea is that a decision tree will divide a data set into sections - visually this can be understood as drawing boxes over a scatter plot of features. It does so by creating decision points, which can be thought of as questions, at points which give most information gain by dividing the data set there. Information gain means that there is variation underneath that decision point that divides the data set and one measure of it is relative entropy. The splits are leaves of a tree constructed by the algorithm consisting of questions (usually yes-no).

The prediction is usually made by saying that the prediction for any new data point falling within a decision box (terminal leaf) is the average of the existing data points in that box. The decision points (questions) are leaves and the prediction areas are terminal leaves.

Since predictions come from allocations to terminal leaves, we would expect a plot of decision tree regression predictions to be blocky. Depending upon the number of terminal leaves it may require a high resolution to see this.

No feature scaling is required for decision trees since the having a large magnitude feature won't cause that feature to dominate a decision tree model. 