from fpgrowth import find_frequent_patterns
import pandas as pd
transactions = [[1, 2, 5],
                [2, 4],
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