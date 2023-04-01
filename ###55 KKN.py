###55 KKN
import pandas as pd
import matplotlib.pyplot as plt
original_data=pd.read_csv("C:/Users/Şebnem\Desktop/tutorials/cancer_data.csv")
data=original_data.copy()
data=data.drop(columns=["id","Unnamed: 32"],axis=1)
M=data[data["diagnosis"]=="M"]
B=data[data["diagnosis"]=="B"]

plt.scatter(M.radius_mean,M.texture_mean,color="red",label="malignant tumor")
plt.scatter(B.radius_mean,B.texture_mean,color="green",label="benign tumor")
plt.legend()
plt.show()