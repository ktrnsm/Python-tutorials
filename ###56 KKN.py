###56 KKN
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

original_data=pd.read_csv("C:/Users/Şebnem\Desktop/tutorials/cancer_data.csv")
data=original_data.copy()
data=data.drop(columns=["id","Unnamed: 32"],axis=1)

data.diagnosis=[1 if code=="M" else 0 for code in data.diagnosis]
y=data["diagnosis"]
X=data.drop(columns="diagnosis",axis=1)
sc=StandardScaler()
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
model=KNeighborsClassifier(n_neighbors=9)
model.fit(X_train,y_train)
prediction=model.predict(X_test)

acs=accuracy_score(y_test,prediction)
print(acs*100)

success=[]
for k in range(1,20):
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train,y_train)
    prediction2nd=knn.predict(X_test)
    success.append(accuracy_score(y_test,prediction2nd))

print(max(success))

plt.plot(range(1,20),success)
plt.xlabel("K")
plt.ylabel("Success")
plt.show()


