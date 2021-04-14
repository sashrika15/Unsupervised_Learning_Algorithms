### Apriori Algorithm

Apriori is used for frequent itemset mining over relational databases. It uses prior knowledge of frequent itemset properties.

Some terms we need to know before implementing Apriori:

Consider items I1 and I2 in a dataset consisting of transactions with the corresponding items bought:
- Support (I1): Ratio between the number of transactions containing the item by the total number of transactions 

- Confidence (I1 => I2): Total number of transactions containing both items I1 and I2 divided by the total number of transactions containing I1.

- Lift (I1 => I2): Ratio between confidence and support

- Frequent Itemset: An itemset whose support value is greater than a given minimum support value.


### How does it work?

Apriori says that: 

- All subsets of a frequent itemset must be frequent.
- If an itemset is infrequent, all its supersets will be infrequent.

Apriori determines k-itemsets (starting with 1) at each step then checks if it is a frequent itemset or not. This includes finding the subsets ot the itemset and ensuring that those are frequent as well. 

This goes on until the most frequent itemset is reached.

### Example
In the image shown below, our datasets consists of 5 transactions containing some items. 

The first itemset is formed by grouping one item. The itemset {4} has a support value less than the given minimum support value (i.e 2), hence it is eliminated. 

This process is repeated to until no more frequent itemsets can be formed.

<img src="https://github.com/sashrika15/Unsupervised_Learning_Algorithms/blob/master/apriori/sample.jpg" width="800">


Contributed by: [Sashrika Surya](https://github.com/sashrika15)
