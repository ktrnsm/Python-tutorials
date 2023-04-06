###99 eclat
import pandas as pd
from pyECLAT import ECLAT
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori,association_rules
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/GroceryStoreDataSet.csv",header=None)
data=original_data.copy()
data.columns=["Product"]
data=list(data["Product"].apply(lambda x:x.split(",")))

data_2nd=pd.DataFrame(data)
#print(data_2nd)

min_product=2
min_support=0.2
max_product=max([len(x) for x in data])

ec=ECLAT(data_2nd,verbose=True)
a,b=ec.fit(min_support=min_support,min_combination=min_product,max_combination=max_product)
print(b)