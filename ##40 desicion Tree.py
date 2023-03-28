##40 desicion Tree
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor,plot_tree
import matplotlib.pyplot as plt
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/Position_Salaries.csv")
data=original_data.copy()
y=data["Salary"]
X=data["Level"]
y=np.array(y).reshape(-1,1)
X=np.array(X).reshape(-1,1)
dt=DecisionTreeRegressor(random_state=0,max_leaf_nodes=5)
dt.fit(X,y)
prediction=dt.predict(X)
plt.figure(figsize=(20,10),dpi=100)
plot_tree(dt,feature_names="Level", class_names="Salary",rounded=True,filled=True)
#plt.scatter(X,y,color="red")
#plt.plot(X,prediction)
plt.show()
