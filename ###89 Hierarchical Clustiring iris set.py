###89 Hierarchical Clustiring iris set
import pandas as pd
import os
from scipy.cluster.hierarchy import dendrogram,linkage
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import seaborn as sns
os.environ['JOBLIB_TEMP_FOLDER'] = 'C:/joblib_temp_folder'

original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/Iris.csv")
data=original_data.copy()
#print(data)
X=data.drop(columns=["Id","Species"],axis=1)
"""
hc_single=linkage(X,method="single")
hc_complete=linkage(X,method="complete")
hc_average=linkage(X,method="average")
hc_centroid=linkage(X,method="centroid")
hc_median=linkage(X,method="median")
hc_ward=linkage(X,method="ward")

fig,axes=plt.subplots(2,3)
dendrogram(hc_single,ax=axes[0,0])
axes[0,0].set_title("Single")
dendrogram(hc_complete,ax=axes[0,1])
axes[0,1].set_title("Complete")
dendrogram(hc_average,ax=axes[0,2])
axes[0,2].set_title("Average")
dendrogram(hc_centroid,ax=axes[1,0])
axes[1,0].set_title("Centroid")
dendrogram(hc_median,ax=axes[1,1])
axes[1,1].set_title("Median")
dendrogram(hc_ward,ax=axes[1,2])
axes[1,2].set_title("Ward")
"""
model=AgglomerativeClustering(n_clusters=2,linkage="ward")
prediction=model.fit_predict(X)
#print(X)
#print(prediction)
#plt.legend()
#plt.show()
labels=model.labels_
#print(labels)
sns.scatterplot(x="SepalLengthCm",y="SepalWidthCm",data=X,hue=labels,palette="deep")
plt.show()

