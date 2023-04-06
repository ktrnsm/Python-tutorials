###96 Apriori
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori,association_rules
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/GroceryStoreDataSet.csv",header=None)
data=original_data.copy()
data.columns=["Product"]
data=list(data["Product"].apply(lambda x:x.split(",")))
#print(data)

te=TransactionEncoder()
te_data=te.fit_transform(data)
data=pd.DataFrame(te_data,columns=te.columns_)
df1=apriori(data,min_support=0.05,use_colnames=True)
#print(df1)
df2=association_rules(df1,metric="confidence",min_threshold=0.5)
print(df2)