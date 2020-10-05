## FP Growth Implementation in Python

This is a python implementation of the FP Growth algorithm to find patterns and associations

### Requirements

1. Python >= 3.6
2. Pandas >= 1.1.0

### Usage

Data has to be in the form of sequence of IDs.

``` 
from fpgrowth import find_frequent_patterns
from fpgrowth import generate_association_rules
import pandas as pd
transactions = [[1, 2, 7],
                [2, 6],
                [2, 3],
                [1, 2, 4],
                [1, 3],
                [2, 3],
                [1, 3],
                [1, 2, 3, 5],
                [1, 2, 3]]

patterns = find_frequent_patterns(transactions, 2)
new = pd.DataFrame.from_dict(patterns, orient='index')
print(new.head())
rules = pyfpgrowth.generate_association_rules(patterns, 0.7)
new2 = pd.DataFrame.from_dict(rules, orient='index')
print(new2.head())
```
### Output
