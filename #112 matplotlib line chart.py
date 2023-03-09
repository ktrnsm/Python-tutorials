#112 matplotlib line chart
import matplotlib.pylab as plt
import numpy as np

plt.figure()
plt.axis()
#plt.show()
plt.xlabel("Year")
plt.ylabel("Qty")
plt.title("sample graph")

x=["2018","2019","2020","2021","2022","2023"] # sayısal alır
#y=np.linspace(100,1000,6)
y=[100,200,600,180,45,1200]
z=y-np.mean(y) # y- y ortalama
plt.plot(x,y)
plt.plot(x,z)   
plt.show()