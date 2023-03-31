###53 logistic regression
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score



original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/winequality-red.csv")
data=original_data.copy()
#print(data)
#print(data.isnull().sum())
#print(data["quality"].unique())

category=["3","4","5","6","7","8"]
oe=OrdinalEncoder(categories=[category])
data["My assumed quality"]=oe.fit_transform(data["quality"].values.reshape(-1,1))
#print(data)
#print(data[data["quality"]==7][["quality","My assumed quality"]])
y=data["My assumed quality"]
X=data.drop(columns="My assumed quality",axis=1)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)


model=LogisticRegression(random_state=0,max_iter=1000)
model.fit(X_train,y_train)
prediction=model.predict(X_test)

cm=confusion_matrix(y_test,prediction)
acs=accuracy_score(y_test,prediction)

print(cm)
print(acs*100)
