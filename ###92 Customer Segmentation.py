###92 Customer Segmentation 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans,AgglomerativeClustering
from yellowbrick.cluster import KElbowVisualizer
#original_data=pd.read_excel("C:/Users/Şebnem/Desktop/tutorials/Online Retail.xlsx")
#original_data.to_csv("C:/Users/Şebnem/Desktop/tutorials/Online Retail.csv",index=False)
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/Online Retail.csv")
data=original_data.copy()
#print(data)

#print(data.isnull().sum())
data=data.dropna()
data["TotalCost"]=data["Quantity"]*data["UnitPrice"]
#print(data)

#print(data[data["TotalCost"]<=0])
data=data.drop(data[data["TotalCost"]<=0].index)
#sns.boxplot(data["TotalCost"])
#plt.show()

Q1=data["TotalCost"].quantile(0.25)
Q3=data["TotalCost"].quantile(0.75)
IQR=Q3-Q1
lower_limit=Q1-1.5*IQR
upper_limit=Q3+1.5*IQR
data=data[~((data["TotalCost"]>upper_limit) | (data["TotalCost"]<lower_limit))]
#print(data.shape)
data=data.reset_index(drop=True)
#print(data)
#print(len(data["CustomerID"].unique()))
#print(data["InvoiceNo"].nunique())
#print(data.info())
data["CustomerID"]=data["CustomerID"].astype("int")
data["InvoiceDate"]=pd.to_datetime(data["InvoiceDate"])

today=data["InvoiceDate"].max()
#print(today)
today=dt.datetime(2011,12,9,12,50,0)

r=(today-data.groupby("CustomerID").agg({"InvoiceDate":"max"})).apply(lambda x:x.dt.days)
#print(r)
f=data.groupby(["CustomerID","InvoiceNo"]).agg({"InvoiceNo":"count"})
f=f.groupby("CustomerID").agg({"InvoiceNo":"count"})
#print(f)

m=data.groupby("CustomerID").agg({"TotalCost":"sum"})
#print(m)

RFM=r.merge(f,on="CustomerID").merge(m,on="CustomerID")
RFM=RFM.reset_index()
RFM=RFM.rename(columns={"CustomerID":"Customer","InvoiceDate":"Recency","InvoiceNo":"Frequency","TotalCost":"Monatery Value"})

df=RFM.iloc[:,1:]
sc=MinMaxScaler()
df_norm=sc.fit_transform(df)
df_norm=pd.DataFrame(df_norm,columns=df.columns)
#print(df_norm.describe())

k_model=KMeans(n_clusters=4,init="k-means++")
k_fit=k_model.fit(df_norm)
labels=k_fit.labels_
RFM["Labels"]=labels
sns.scatterplot(x="Labels",y="Customer",data=RFM,hue=labels,palette="deep")
#plt.xlim([-1,5])
#plt.show()

#print(RFM.groupby("Labels")["Customer"].count())
print(RFM.groupby("Labels").mean().iloc[:,1:])
#sns.scatterplot(x="Recency", y="Frequency", data=df_norm, palette="deep",hue=labels)
#plt.show()
#chart=KElbowVisualizer(k_model,k=(2,10))
#chart.fit(df_norm)
#chart.poof()