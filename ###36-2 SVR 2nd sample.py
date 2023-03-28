###36-2 SVR 2nd sample
import yfinance as yf
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import sklearn.metrics as mt
from sklearn.model_selection import GridSearchCV
apple_data=yf.download("AAPL",start="2023-01-01",end="2023-02-01")
data=apple_data.copy()
data=data.reset_index()
print(data.columns)
data["Day"] = data["Date"].astype(str).str.split("-").str[2]
y=data["Adj Close"]
X=data["Day"]
y=np.array(y).reshape(-1,1)
X=np.array(X).reshape(-1,1)
scy=StandardScaler()
scx=StandardScaler()
X=scx.fit_transform(X)
y=scy.fit_transform(y)

svr_rbf=SVR(kernel="rbf",C=100,gamma=1)
svr_rbf.fit(X,y)
prediction_rbf=svr_rbf.predict(X)

svr_linear=SVR(kernel="linear")
svr_linear.fit(X,y)
prediction_linear=svr_linear.predict(X)

svr_poly=SVR(kernel="poly")
svr_poly.fit(X,y)
prediction_poly=svr_poly.predict(X)
r2=mt.r2_score(y,prediction_rbf)
rmse=mt.mean_squared_error(y,prediction_rbf,squared=False)
print("R2:{} RMSE:{}".format(r2,rmse))

#parameters={"C":[1,10,100,1000,10000],"gamma":[1,0.1,0.001],"kernel":["rbf","linear","poly"]}
#tunning=GridSearchCV(estimator=SVR(),param_grid=parameters,cv=10)
#tunning.fit(X,y)
#print(tunning.best_params_)


plt.scatter(X,y,color="blue")
plt.plot(X,prediction_rbf,color="red",label="RBF MODEL")
#plt.plot(X,prediction_linear,color="blue",label="LINEAR MODEL")
#plt.plot(X,prediction_poly,color="black",label="POLY MODEL")
plt.legend()
plt.show()