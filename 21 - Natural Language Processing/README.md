# Natural Language Processing

The aim of this section is to illustrate how to:

-Clean texts to prepare them for the Machine Learning models
-Create a Bag of Words model
-Apply Machine Learning models onto this Bag of Words model

The tsv file contains restaurant reviews. The 1 and 0 values reflect positive or negative reviews. A tsv is used because reviews contain commas.

The aim is to train a model which can accurately decide from the text of a review whether that review is positie or negative.

The bag of words model will decide based upon relevant words rather than neutral words such as 'is', 'the' or 'this'. We will strip these words and also strip punctuation.

We employ stemming to unify different words that fall under the same root e.g. 'Love' and 'Loved'.

The reviews get tokenised, meaning that they are broken into a collection of only relevant words so that a weighted model can be built around the reviews based on the frequency of occurrence of words in positive or negative reviews.

Once the reviews are tokenised in a bag of words model, the predictions can be made using a classification learning model. Typical classification models for NLP scenarios are Naive Bayes or Random Forest.