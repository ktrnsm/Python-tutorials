import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
data = pd.read_excel("C:/Users/Şebnem/Desktop/tutorials/###6.xlsx")
y = data["Y"]
X = data[["X1", "X2"]]
X = sm.add_constant(X)  # add constant term for intercept
model = sm.OLS(y, X).fit()
#print(model.summary())

prediction=model.predict(X)
#print(prediction)
MSE=mean_squared_error(y,prediction)
RMSE=mean_squared_error(y,prediction,squared=False)
MAE=mean_absolute_error(y,prediction)
print(MSE)
print(RMSE)
print(MAE)
