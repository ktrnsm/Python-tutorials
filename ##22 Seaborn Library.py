##22 Seaborn Library
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

x=np.random.normal(35,1,10000)
#plt.hist(x)
#plt.show()
#sns.histplot(x)
sns.displot(x,kde=True,color="gray")
sns.kdeplot(x) # sadece grafiği gösterir.
plt.show()