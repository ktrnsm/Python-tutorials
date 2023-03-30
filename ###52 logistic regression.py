###52 logistic regression
import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score


original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/Iris.csv")
data=original_data.copy()
data=data.drop(columns="Id",axis=1)
#print(data)
#print(data.isnull())
#print(data.info())
#print(data["Species"].unique())
#print(len(data["Species"].unique()))

le=LabelEncoder()
data["Species"]=le.fit_transform(data["Species"])
#print(data)

y=data["Species"]
X=data.drop(columns="Species",axis=1)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

model=LogisticRegression(random_state=0)
model.fit(X_train,y_train)
prediction=model.predict(X_test)
cm=confusion_matrix(y_test,prediction)
ac=accuracy_score(y_test,prediction)

print(cm)
print(ac)

cv=cross_val_score(model,X_test,y_test,cv=10).mean()
print(cv)
