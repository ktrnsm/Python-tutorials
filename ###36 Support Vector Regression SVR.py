###36 Support Vector Regression SVR
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import matplotlib.pyplot as plt
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/Position_Salaries.csv")
data=original_data.copy()
y=data["Salary"]
X=data["Level"]
y=np.array(y).reshape(-1,1)
X=np.array(X).reshape(-1,1)
scx=StandardScaler()
scy=StandardScaler()
y=scy.fit_transform(y)
X=scx.fit_transform(X)
svrmodel=SVR(kernel="rbf")
svrmodel.fit(X,y)
prediction=svrmodel.predict(X)
plt.scatter(X,y,color="red")
plt.plot(X,prediction)
plt.show()