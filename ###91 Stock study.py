###91 Stock study
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import KMeans, AgglomerativeClustering
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram

original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/stock.csv")
data=original_data.copy()

ms=MinMaxScaler()
X=ms.fit_transform(data.iloc[:,[1,2]])
X=pd.DataFrame(X,columns=["Income","Voliality"])

hc=linkage(X,method="single")
dendrogram(hc)
plt.show()

model=AgglomerativeClustering(n_clusters=3,linkage="single")
prediction=model.fit_predict(X)
labels=model.labels_
data["Labels"]=labels

sns.scatterplot(x="Labels",y="Stock",data=data,hue="Labels",palette="deep")
plt.show()
#k_model=KMeans(random_state=0,n_clusters=6)
#k_fit=k_model.fit(X)
#labels=k_fit.labels_



#sns.scatterplot(x="Income",y="Voliality",data=X,hue=labels,palette="deep")
#plt.show()
#chart=KElbowVisualizer(k_model,k=(2,20))
#chart.fit(X)
#chart.poof()



