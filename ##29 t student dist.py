##29  student's t dist

from scipy import stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

np.random.seed(0)
data1t=stats.t.rvs(loc=0,df=1,size=15)
data2t=stats.t.rvs(loc=0,df=2,size=15)
data3t=stats.t.rvs(loc=0,df=5,size=15)
data4t=stats.t.rvs(loc=0,df=20,size=15)

plt.xlim(-5,5)
sns.distplot(data1t,hist=False,color="red") #eğriyi kendisi çiziyor. hist false histogram'ı iptal ediyor.
sns.distplot(data2t,hist=False,color="blue")
sns.distplot(data3t,hist=False,color="green")
sns.distplot(data4t,hist=False,color="gray")

plt.show()