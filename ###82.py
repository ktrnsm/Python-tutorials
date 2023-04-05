import pandas as pd
import os
import matplotlib.pylab as plt
import seaborn as sns
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer

os.environ['JOBLIB_TEMP_FOLDER'] = 'C:/joblib_temp_folder'
original_data = pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/Mall_Customers.csv")
data = original_data.drop(columns="CustomerID")
X = data.iloc[:, 1:3]

kmodel = KMeans(random_state=0)
chart = KElbowVisualizer(kmodel, k=(1,20))
chart.fit(X)
chart.show()
