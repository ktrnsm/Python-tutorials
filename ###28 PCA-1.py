###28PCA-1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split,KFold,cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
import sklearn.metrics as mt
import numpy as np
original_data=pd.read_csv("C:/Users/Şebnem\Desktop/tutorials/winequality-red.csv")
data=original_data.copy()
#print(data)
#print(data.isnull().sum())
#print(data.info())
#cor=data.corr()
#sns.heatmap(cor,annot=True,cbar=True)
#plt.show()

y=data["quality"]
X=data.drop(columns="quality",axis=1)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
pca=PCA(n_components=4)
X_train2nd=pca.fit_transform(X_train)
X_test2nd=pca.transform(X_test)

#print(X_train.shape)
#print(X_train2nd.shape)
#print(np.cumsum(pca.explained_variance_ratio_)*100)
#plt.plot(np.cumsum(pca.explained_variance_ratio_))
#plt.xlabel("Number of Components.")
#plt.ylabel("Explained variance")
#plt.show()

lm=LinearRegression()
lm.fit(X_train2nd,y_train)
prediction=lm.predict(X_test2nd)
r2=mt.r2_score(y_test,prediction)
rmse=mt.mean_squared_error(y_test,prediction,squared=True)
print("R2:{} RMSE:{}".format(r2,rmse))

cv=KFold(n_splits=10,shuffle=True,random_state=1)
lm2nd=LinearRegression()
RMSE=[]
for i in range(1,X_train2nd.shape[1]+1):
    failure=np.sqrt(-1*cross_val_score(lm2nd,X_train2nd[:,:i],y_train.ravel(),
                                       cv=cv,scoring="neg_mean_squared_error").mean())
    RMSE.append(failure)
#plt.plot(RMSE,"-x")
#plt.xlabel("Number of Components")
#plt.ylabel("RMSE")
#plt.show()
