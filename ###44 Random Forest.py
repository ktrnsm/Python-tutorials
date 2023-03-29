###44 Random Forest
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/###14.csv")
data=original_data.copy()

y=data["Sales"]
X=data.drop(columns="Sales",axis=1)

#y=np.array(y).reshape(-1,1)
#X=np.array(X).reshape(-1,1)

dt_model=DecisionTreeRegressor(random_state=0)
dt_model.fit(X,y)
dt_prediction=dt_model.predict(X)

rf_model=RandomForestRegressor(random_state=0)
rf_model.fit(X,y)
rf_prediction=rf_model.predict(X)

plt.scatter(X,y,color="red")
plt.plot(X,rf_prediction,color="blue")
plt.plot(X,dt_prediction,color="green")

plt.show()