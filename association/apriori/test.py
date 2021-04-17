import pandas as pd 
from apriori import Apriori

# Path to dataset
path = "data/groceries.csv"

# Reading dataset
groceries_file = pd.read_csv(path,names=["Items"],header = None , sep =";")

# Building list of data items
data = []
sentences = list(groceries_file['Items'])
for sen in sentences:
    data.append(sen)

# Building list of transactions
transactions = []
for a in data:
    transactions.append(set(a.split(',')))

print("Total transactions in dataset:",len(transactions))

# Defining threshold and minimum count of items for rule to qualify
threshold=0.5
mincount = 10

# Initialising Apriori class
model = Apriori(transactions,threshold,mincount)

# Finding final rules
final_rules = {}
final_rules = model.find_assoc_rules()

print("\nFound {} rules whose confidence exceeds {}.\n".format(len(final_rules), threshold))

# Printing final rules
model.print_rules(final_rules)

