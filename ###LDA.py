###LDA
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np

original_data=pd.read_csv("C:/Users/Şebnem\Desktop/tutorials/winequality-red.csv")
data=original_data.copy()
y=data["quality"]
X=data.drop(columns="quality",axis=1)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
lda=LinearDiscriminantAnalysis()
X_train2nd=lda.fit_transform(X_train,y_train)
X_test2nd=lda.transform(X_test)
print(np.cumsum(lda.explained_variance_ratio_)*100)
print(len(np.unique(y_train)))