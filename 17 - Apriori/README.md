# A Priori Association Rule Learning

This example is about optimising the number of sales at a grocery store in the south of France. The idea is to locate cases where a customer purchasing a particular product is likely to purchase another. This enables better product placement (e.g. placing cereal next to milk).

Each row is a shopping list of sorts - it is the list of products (product names) bought by a particular customer. It is one week's transactions in a sparse form (blanks are omitted).

A better representation might be if we  one column per product. Entries should be 0 or 1, depending upon whether product purchased. But instead we have a representation with product names for purchases and no entry for not purchased items.

The data set needs to be transformed to fit the expected input of the algorithm implementation (and is in the example code).  

The steps for the A Priori Association Rule Learning algorithm are:

1 Set a minimum support and confidence.
2 Take all the subsets in transactions having higher support than minimum support.
3 Take all the rules of these subsets having higher confidence than minimum confidence.
4 Sort the rules by decreasing lift.

The support of a set of items i is the number of transactions containing those items divided by total number of transactions. So setting minimum support is a way of saying that rules should only be learned on items that appear frequently enough in the transactions (the value is a proportion).

The confidence is a measure of the strength of the association. It is the proportion of transactions for which the rule holds. Setting a minimum allows us to filter rules to only strong enough associations. 

Lift is a measure of the strength of the rule. It is the deviation from the occurrence one would expect anyway if the items were appearing in transactions randomly with an independent relationship. A value greater than one is better than chance, whereas less than one could indicate a negative relationship.