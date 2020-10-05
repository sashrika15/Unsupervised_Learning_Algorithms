from fpgrowth import find_frequent_patterns
from fpgrowth import generate_association_rules
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
rules = generate_association_rules(patterns, 0.7)

