###100 detailed apriori - eclat study project

import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/Online Retail.csv")
data=original_data.copy()
#print(data.isnull().sum())
data=data.dropna()
data=data[~data["InvoiceNo"].str.contains("C")]
#print(data)

data_2nd=data["Country"].value_counts()
#print(data_2nd)

country=data[data["Country"]=="United Kingdom"]
basket=country.iloc[:,[0,2,3]]
basket=basket.groupby(["InvoiceNo","Description"])["Quantity"].sum().unstack().reset_index().fillna(0).set_index("InvoiceNo")

   
basket_arranged = basket.applymap(lambda x: 0 if x <= 0 else 1)
#print(basket_arranged)
#print(basket)

df1=apriori(basket_arranged.astype("bool"),min_support=0.02,use_colnames=True)
df2=association_rules(df1,metric="confidence")
print(df2.iloc[0])
