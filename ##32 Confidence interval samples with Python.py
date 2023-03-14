##32 Confidence interval samples with Python
import numpy as np
from scipy import stats

##1
"""Sample size (n) = 100 products
Sample mean weight (x̄) = 1040 g
Sample standard deviation (s) = 25 g
Desired level of confidence = 95%, which corresponds to a z-score of 1.96 for a two-tailed test."""

n=100
xav=1040
xstd=25
confInter=0.95
range=stats.norm.interval(confInter,loc=xav,scale=xstd/np.sqrt(n))
print(range)

##2
n=85
xav=67
xstd=14
confInter=0.95

range2=stats.norm.interval(confidence=confInter,loc=xav,scale=xstd/np.sqrt(n))
print (range2)

##3
n=16
xstd=2
xav=4
confInter=0.95

range3=stats.norm.interval(confidence=0.95,loc=xav,scale=xstd/np.sqrt(n))
print(range3)

##4
n=25
xav=120
var=100
xstd=var**0.5
confInter=0.90
confInter2=0.99
range4=stats.norm.interval(confidence=0.90,loc=xav,scale=xstd/np.sqrt(n))
range5=stats.norm.interval(confidence=0.99,loc=xav,scale=xstd/np.sqrt(n))

print(range4)
print(range5)

##5
n=100
xav=385
std=12
confInter=0.95
range6=stats.norm.interval(confidence=0.95,loc=xav,scale=xstd/np.sqrt(n))
print(range6)


