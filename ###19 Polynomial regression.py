###19-20-21 Polynomial regression.
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import sklearn.metrics as mt
from sklearn.preprocessing import PolynomialFeatures
original_data=pd.read_excel("C:/Users/Şebnem/Desktop/tutorials/###19.xlsx")
data=original_data.copy()
#print(data)

y=data["Efficiency"]
X=data["Heat"]
y=y.values.reshape(-1,1)
X=X.values.reshape(-1,1)

lr=LinearRegression()
lr.fit(X,y)
prediction=lr.predict(X)
r2_linear=mt.r2_score(y,prediction)
mse_linear=mt.mean_squared_error(y,prediction)
print("Linear R2: {} Linear MSE: {}".format(r2_linear,mse_linear))

pol=PolynomialFeatures(degree=3)
X_pol=pol.fit_transform(X)
lr2nd=LinearRegression()
lr2nd.fit(X_pol,y)
prediction2nd=lr2nd.predict(X_pol)

r2_pol=mt.r2_score(y,prediction2nd)
mse_pol=mt.mean_squared_error(y,prediction2nd)

print("Pol R2: {} Pol MSE: {}".format(r2_pol,mse_pol))

plt.scatter(X,y,color="blue")
plt.plot(X,prediction2nd,color="red")
plt.show()


