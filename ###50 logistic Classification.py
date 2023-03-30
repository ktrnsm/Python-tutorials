###50 logistic Classification
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

original_data=pd.read_csv("C:/Users/Şebnem\Desktop/tutorials/cancer_data.csv")
data=original_data.copy()
#print(data.isnull().sum())
#print(data.info())
data=data.drop(columns=["id","Unnamed: 32"],axis=1)
#print(data)

y=data["diagnosis"]
X=data.drop(columns="diagnosis",axis=1)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

model=LogisticRegression(random_state=0)
model.fit(X_train,y_train)
prediction=model.predict(X_test)
print(prediction)