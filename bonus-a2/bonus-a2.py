import numpy as np
import matplotlib.pyplot as pyplot
import pandas as pd
from apyori import apriori
import pyfpgrowth as fp



data = pd.read_csv('data.csv', header=None)
print("here")
print(data.head())
y = len(data.columns)
# print("y is:",y)
records = []
# print(len(data))
for i in range(0, len(data)):
    x = []
    for j in range(0,y):
        if(str(data.values[i,j]) != 'nan'):
            x.append(str(data.values[i,j]))
    records.append(x)
print("Apriorio Algorithm:")
association_rules = apriori(records, min_support=0.0045, min_confidence = 0.2, min_lift=3, min_length=2)
association_results = list(association_rules)
print(len(association_results))
print(association_results[0])
print("------------------------------")
print(association_results[0])
for item in association_results:
    pair = item[0]
    items = [x for x in pair]
    if('nan' not in items):
        print("Rule:" + items[0] + " -> " + items[1])
        print("Support: "+str(items[1]))
        print("Confidence: "+str(item[2][0][2]))
        print("Lift: "+str(item[2][0][3]))
        print("------------------------------")


print("Partition Algorithm Frequent Items:")

result = fp.find_frequent_patterns(records, 25)
print("Frequency pattern:")

print(result)
assoc_rules = fp.generate_association_rules(result, 0.6)
print("--------------------")
print("Association Rules:")
keys = assoc_rules.keys()
for key in keys:
    print(key," -> ",assoc_rules[key][0],":",assoc_rules[key][1])
    