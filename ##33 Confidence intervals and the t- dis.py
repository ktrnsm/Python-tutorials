##33 Confidence intervals and the t- distribution
#standart sapmanın bilinmediği varsayımı altında papülasyonun güven aralığı bu şekilde tespit ediliyor.


import numpy as np
from scipy import stats
n=30
xav=140
xsdev=25
conf=0.95
svalue=n-1
interval=stats.t.interval(0.95,loc=xav,df=svalue,scale=xsdev/np.sqrt(n))
print(interval)