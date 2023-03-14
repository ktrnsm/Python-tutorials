##34 Confidence Interval for the Difference between Two Population Means.
import numpy as np
from scipy import stats

#At a production for two  different products

vara=164
varb=216
na=28
nb=30
meana=32
meanb=26
confint=0.95
#find the average weight difference of a, for the %95 Confidential interval
interval=stats.norm.interval(0.95,loc=(meana-meanb),scale=np.sqrt((vara/na)+(varb/nb)))
print(interval) #between the two result values
#(-1.0822649344425628, 13.082264934442563)


# two student group selected
nEng=30
nFr=40
Engmean=182
Frmean=176
varEn=196
varFr=144
conf=0.95
#find the learning day difference between two group for %95 confidential interval
interv=stats.norm.interval(0.95,loc=(Engmean-Frmean),scale=np.sqrt((varEn/nEng)+(varFr/nFr)))
print(interv)

