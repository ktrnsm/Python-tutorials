###86 Hierarchical Clustering
import pandas as pd
import os
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

os.environ['JOBLIB_TEMP_FOLDER'] = 'C:/joblib_temp_folder'
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/Mall_Customers.csv")
data=original_data.copy()

X=data.iloc[:,2:4]
#print(X)

model=AgglomerativeClustering()
prediction=model.fit_predict(X)
#print(prediction)
X["label"]=prediction
#print(X)
#plt.scatter(X["Age"][X["label"]==0],X["Annual Income (k$)"][X["label"]==0],c="red")
#plt.scatter(X["Age"][X["label"]==1],X["Annual Income (k$)"][X["label"]==1],c="black")
#plt.show()

link=linkage(X)
dendrogram(link)
plt.xlabel("Data Dotes")
plt.ylabel("Measurements")
plt.show()
