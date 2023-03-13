##24 Z Table
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

np.random.seed(0)
data=np.random.normal(35,2,40000) #ortalama 35, standart sapma=2, 5 elemanlı bir veri seti oluşturur.
#her seferinde yeni küme oluşturur. bunu egnellemek için seed kullanırız.
data2nd=(data-np.mean(data))/np.std(data)
data3rd=stats.zscore(data)
sns.displot(data,kde=True)
sns.displot(data2nd,kde=True)
plt.title("Data Dis. Chart",fontsize=15,loc="right", c="red")
plt.xlabel("Data",fontsize=15,c="red")
plt.ylabel("Rate",fontsize=15,c="red")
plt.xlim(-3,3)
plt.axvline(x=np.mean(data2nd),linestyle="--",linewidth=2.5,label="mean",c="red")
plt.axvline(x=np.mean(data2nd)-np.std(data),linestyle="-",linewidth=1.5,label="std",c="black")
plt.axvline(x=np.mean(data2nd)+np.std(data),linestyle="-",linewidth=1.5,c="black")
plt.axvline(x=np.mean(data2nd)-2*np.std(data),linestyle="-",linewidth=1.5,c="orange")
plt.axvline(x=np.mean(data2nd)+2*np.std(data),linestyle="-",linewidth=1.5,label="2 std",c="orange")


plt.legend()
plt.show()