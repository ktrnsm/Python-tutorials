###27 linear regression - ridge lasso elasticNEt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm
from sklearn.model_selection import train_test_split, cross_val_score
import sklearn.metrics as mt
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet



original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/USA_Housing.csv")
data=original_data.copy()
#print(data)
data=data.drop(columns="Address",axis=1)
#print(data.isnull().sum())
#sns.pairplot(data)
#plt.show()

#cor=data.corr()
#sns.heatmap(cor,annot=True)
#plt.show()

y=data["Price"]
X=data.drop(columns="Price",axis=1)
stbl=sm.add_constant(X)
vif=pd.DataFrame()
vif["variables"]=X.columns
vif["VIF"]=[variance_inflation_factor(stbl,i+1)for i in range(X.shape[1])]
#print(vif)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

def crossvalidation(model):
    validation=cross_val_score(model,X,y,cv=10)
    return validation.mean()

def success(real,prediction):
    rmse=mt.mean_squared_error(real,prediction,squared=True)
    r2=mt.r2_score(real,prediction)
    return [rmse,r2]

linear_model=LinearRegression()
linear_model.fit(X_train,y_train)
linear_prediction=linear_model.predict(X_test)

ridge_model=Ridge(alpha=0.1)
ridge_model.fit(X_train,y_train)
ridge_prediction=ridge_model.predict(X_test)

lasso_model=Lasso(alpha=0.1)
lasso_model.fit(X_train,y_train)
lasso_prediction=lasso_model.predict(X_test)

elasticNet_model=Lasso(alpha=0.1)
elasticNet_model.fit(X_train,y_train)
elasticNet_prediction=elasticNet_model.predict(X_test)

results=[["Linear Model",success(y_test,linear_prediction)[0],success(y_test,linear_prediction)[1],crossvalidation(linear_model)],
         ["Ridge Model",success(y_test,ridge_prediction)[0],success(y_test,ridge_prediction)[1],crossvalidation(ridge_model)],
         ["Lasso Model",success(y_test,lasso_prediction)[0],success(y_test,lasso_prediction)[1],crossvalidation(lasso_model)],
         ["ElasticNet Model",success(y_test,elasticNet_prediction)[0],success(y_test,elasticNet_prediction)[1],crossvalidation(elasticNet_model)]]

pd.options.display.float_format='{:.4f}'.format
results=pd.DataFrame(results,columns=["Model","RMSE","R2","VALIDATION"])
print(results)

