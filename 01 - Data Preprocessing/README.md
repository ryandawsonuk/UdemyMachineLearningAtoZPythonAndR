#Preprocessing

The aim of this module is to prepare the data so that we can go on to apply machine learning to it.

#Data
The dataset represents data on customers and whether they purchased a product. The customer features are age, country and salary.

#Splitting the data for training purposes

We'll want to use part of the data set to train a learner and part to then test the trained learner (so as to avoid overfitting). The function train_test_split in sklearn.cross_validation is used to do this, using an 80:20 train:test split. For R the function split in caTools is used.

#Missing Values
There are missing values in the data, which can't be left as they are if we're to use the data to make predictions. The chosen approach is to replace missing values with the mean for the column (rather than remove rows with missing data or use another replacement strategy). In Python this is done using sklearn.preprocessing.Imputer. In R ave is used.

If the missing values were categorical then we might have Imputed using most common value from column but the missing values here are numerical.

#Categorical Data
The purchased Yes/No column can be converted to a numerical representation relatively easily as a 1/0 variable. This is done using sklearn.preprocessing.LabelEncoder.

This is enough for 'Purchased' because it is the indepedent variable which we aim to predict. But for the depedent variables if we use a scale of numeric values then this would be taken by a learner to reflect magnitude. 

So instead the different Country values are transposed into indicators in seperate columns (dummy encoding). In Python we do this using sklearn.preprocessing.OneHotEncoder (sometimes called one-hot encoding). In R this is done by conversion to a factor.

#Scaling
Since we have numerical features (age and salary) we should apply feature scaling as otherwise features with large numerical magnitude (salary in this case) would unfairly dominate the learner. This is done using sklearn.preprocessing.StandardScaler. In R this is done using the scale function.