###17 model tunning
import pandas as pd
from sklearn.model_selection import train_test_split,KFold
from sklearn.linear_model import LinearRegression
import sklearn.metrics as mt

original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/###14.csv")
data=original_data.copy()
#print(data)

y=data["Sales"]
X=data.drop("Sales",axis=1)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

lr=LinearRegression()
model=lr.fit(X_train,y_train)

def score(model,x_train,x_test,y_train,y_test):
    train_prediction=model.predict(x_train)
    test_prediction=model.predict(x_test)

    r2_train=mt.r2_score(y_train,train_prediction)
    r2_test=mt.r2_score(y_test,test_prediction)
    mse_train=mt.mean_squared_error(y_train,train_prediction)
    mse_test=mt.mean_squared_error(y_test,test_prediction)

    return[r2_train,r2_test,mse_train,mse_test]

result1st = score(model=lr, x_train=X_train, x_test=X_test, y_train=y_train, y_test=y_test)


print("Train R2 = {} Train MSE={}".format(result1st[0],result1st[2]))
print("Test R2={} Test MSE={}".format(result1st[1],result1st[3]))

lr_cv=LinearRegression() #cross validation
k=5
iteration=1
cv=KFold(n_splits=k)

for train_index,test_index in cv.split(X):
    X_train,X_test=X.loc[train_index],X.loc[test_index]
    y_train,y_test=y.loc[train_index],y.loc[test_index]
    lr_cv.fit(X_train,y_train)
    result2nd=score(model=lr_cv,x_train=X_train,x_test=X_test,y_train=y_train,y_test=y_test)
    print("Iteration:{}".format(iteration))
    print("Train R2 = {} Train MSE={}".format(result2nd[0],result2nd[2]))
    print("Test R2={} Test MSE={}".format(result2nd[1],result2nd[3]))
    iteration+=1

    



