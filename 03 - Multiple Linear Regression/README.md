#Multiple Linear Regression

Linear regression with multiple variables. Takes data set of startups using variables R&D Spend, Administration, Marketing Spend, State and Profit. Profit is dependent variable.

States are categorical so we use dummy encoding (python) or factor conversion (R) as appropriate. Dummy variable trap is avoided by removing one of the dummied columns (which we do because it is implied by the others).

Backward elimination of features which have least correlation (highest p-value, which can be inspected in R from lm function or OLS in Python). This is continued until a pre-decided threshold for p-value is reached (5%) but an alternative approach would be to continue removing variables so long it improves adjusted R squared.