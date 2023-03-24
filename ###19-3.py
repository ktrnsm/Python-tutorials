import pandas as pd
import matplotlib.pylot as plt
import seaborn as sns
original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/Realestate.csv")
data=original_data.copy()
data.drop(columns=["No","X1 transaction date","X5 latitude","X6 longitude"],axis=1,inplace=True)
data=data.rename(columns={"X2 house age":"house age","X3 distance to the nearest MRT station":"location subway",
                          "X4 number of convenience stores":"location shopping","Y house price of unit area":"house value"})

