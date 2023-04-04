###78
import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split,GridSearchCV
from lazypredict.Supervised import LazyClassifier
from sklearn.svm import LinearSVC,SVC
from sklearn.linear_model import RidgeClassifier,LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score,r2_score,roc_auc_score

os.environ['JOBLIB_TEMP_FOLDER'] = 'C:/joblib_temp_folder'
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/WA_Fn-UseC_-Telco-Customer-Churn.csv")
data=original_data.copy()
data=data.drop(columns="customerID",axis=1)
data["TotalCharges"]=pd.to_numeric(data["TotalCharges"],errors="coerce")


def predict_missing_total_charges(data):
    missing_mask = data['TotalCharges'].isnull()
    missing_X = data.loc[missing_mask, ['MonthlyCharges', 'tenure']].values
    non_missing_X = data.loc[~missing_mask, ['MonthlyCharges', 'tenure']].values
    non_missing_y = data.loc[~missing_mask, 'TotalCharges'].values
    model = LinearRegression()
    model.fit(non_missing_X, non_missing_y)
    missing_y_pred = model.predict(missing_X)
    data.loc[missing_mask, 'TotalCharges'] = missing_y_pred
    return data
data = predict_missing_total_charges(data)
#print(data.isnull().sum())

#print(data.describe())

#plt.boxplot(data["TotalCharges"])
#plt.show()

#print(data.select_dtypes(include="object").columns)

le=LabelEncoder()
varriable=data.select_dtypes(include="object").columns
data.update(data[varriable].apply(le.fit_transform))
data["Churn"]=[1 if code==0 else 0 for code in data["Churn"]]
#print(data)

y=data["Churn"]
X=data.drop(columns="Churn",axis=1)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

#clf=LazyClassifier()
#models,y_pred=clf.fit(X_train,X_test,y_train,y_test)
#order=models.sort_values(by="Accuracy",ascending=False)
#print(models.sort_values(by="Accuracy",ascending=False))


#plt.barh(order.index,order["Accuracy"])
#plt.show()

models=["LinearSVC","SVC","Ridge","Logistic","RandomForest","LGBM","XGBM"]
classes=[LinearSVC(random_state=0,C=0.1,penalty="l2",dual=False),SVC(random_state=0,C=1,gamma=0.01,kernel="rbf",),RidgeClassifier(random_state=0,alpha=0.1),
         LogisticRegression(random_state=0,C=0.1,penalty="l2",dual=False),RandomForestClassifier(max_depth=10,min_samples_split=5,n_estimators=1000),
         LGBMClassifier(random_state=0,learning_rate=0.001,max_depth=4,n_estimators=2000,subsample=0.3),
         XGBClassifier(learning_rate=0.001,max_depth=4,n_estimator=2000,subsample=0.8)]
"""
parameters={
    models[0]:{"C":[0.1,1,10,100],"penalty":["l1","l2"]},
    models[1]:{"kernel":["linear","rbf"],"C":[0.1,1],"gamma":[0.01,0.001]},
    models[2]:{"alpha":[0.1,1.0]},
    models[3]:{"C":[0.1,1],"penalty":["l1","l2"]},
    models[4]:{"n_estimators":[1000,2000],"max_depth":[4,10],"min_samples_split":[2,5]},
    models[5]:{"learning_rate":[0.001,0.01],"n_estimators":[1000,2000],"max_depth":[4,10]},
    models[6]:{"learning_rate":[0.001,0.01],"n_estimators":[1000,2000],"max_depth":[4,10],"subsample":[0.6,0.8]}

}"""

def solution(model):
    model.fit(X_train,y_train)
    return model

def score(model2):
    y_pred=solution(model2).predict(X_test)
    acs=accuracy_score(y_test,y_pred)
    r2=r2_score(y_test,y_pred)
    roc=roc_auc_score(y_test,y_pred)
    return acs*100,r2*100,roc*100
""""
for i,j in zip(models,classes):
    print(i)
    grid=GridSearchCV(solution(j),parameters[i],cv=10,n_jobs=-1)
    grid.fit(X_train,y_train)
    print(grid.best_params_)
    """
success=[]

for i in classes:
    success.append(score(i))

score_list=list(zip(models,success))
result=pd.DataFrame(score_list,columns=["Models", "Success"])
print(result.sort_values("Success",ascending=False))
