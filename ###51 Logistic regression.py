###51 Logistic regression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report,roc_curve,roc_auc_score
import matplotlib.pyplot as plt

original_data=pd.read_csv("C:/Users/Şebnem\Desktop/tutorials/cancer_data.csv")
data=original_data.copy()
data=data.drop(columns=["id","Unnamed: 32"],axis=1)

data.diagnosis=[1 if kod=="M" else 0 for kod in data.diagnosis]
print(data)

y=data["diagnosis"]
X=data.drop(columns="diagnosis",axis=1)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

model=LogisticRegression(random_state=0)
model.fit(X_train,y_train)
prediction=model.predict(X_test)
#print(prediction)

cm=confusion_matrix(y_test,prediction)
acs=accuracy_score(y_test,prediction)
cr=classification_report(y_test,prediction)
auc=roc_auc_score(y_test,prediction)

fpr,tpr,thresold=roc_curve(y_test,model.predict_proba(X_test)[:,1])
plt.plot(fpr,tpr,label="Model AUC(Area=%0.2f)" %auc)
plt.xlabel("False Possitive Rate")
plt.ylabel("True Possitive Rate")
plt.legend(loc="lower right")
plt.plot([0,1],[0,1],"r--")
plt.show()