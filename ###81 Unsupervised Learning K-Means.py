###81 Unsupervised Learning K-Means
import pandas as pd
import os
import matplotlib.pylab as plt
import seaborn as sns
from sklearn.cluster import KMeans

os.environ['JOBLIB_TEMP_FOLDER'] = 'C:/joblib_temp_folder'
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/Mall_Customers.csv")
data=original_data.copy()
data=data.drop(columns="CustomerID",axis=1)
#print(data.isnull().sum())
#print(data.describe())

X=data.iloc[:,1:3]
#plt.scatter(X.iloc[:,0],X.iloc[:,1],color="black")
#plt.show()
kmodel=KMeans(n_clusters=4,random_state=0)
kfit=kmodel.fit(X)
#print(kmodel.cluster_centers_)
clusters=kfit.labels_
centers=kfit.cluster_centers_

figure,axis=plt.subplots(1,2)
axis[0].scatter(X.iloc[:,0],X.iloc[:,1],color="black")
axis[1].scatter(X.iloc[:,0],X.iloc[:,1],c=clusters,cmap="winter")
axis[1].scatter(centers[:,0],centers[:,1],c="red",s=200)
plt.show()

#wcss=[]
#for k in range(1,20):
#    k_trial_model=KMeans(n_clusters=k,random_state=0)
#    k_trial_model.fit(X)
#    wcss.append(k_trial_model.inertia_)

#plt.plot(range(1,20),wcss)
#plt.xlabel("K values")
#plt.ylabel("WCSS")
#plt.show()

