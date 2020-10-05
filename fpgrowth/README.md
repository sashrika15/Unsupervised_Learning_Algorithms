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
rules = generate_association_rules(patterns, 0.7)
```
### Output

Both the above mentioned functions return values hence a variable must be stored each time they are called.

The find_frequent_patterns prints a dataframe:

```
Printing Patterns

           0
(5,)       2
(1, 5)     2
(2, 5)     2
(1, 2, 5)  2
(4,)       2
(2, 4)     2
(1,)       6
(1, 2)     4
(2, 3)     4
(1, 2, 3)  2
(1, 3)     4
(2,)       7

```

The generate_association_rules prints a dataframe:

```
Printing Association 

             0    1
(5,)    (1, 2)  1.0
(1, 5)    (2,)  1.0
(2, 5)    (1,)  1.0
(4,)      (2,)  1.0

```
