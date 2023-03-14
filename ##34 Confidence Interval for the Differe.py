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


#two different illness group
n1=8
n2=10
maean1=3
mean2=2.7
varab=0.05
con=0.95
#find the reaction of the sickness of this two group's time with the confidental interval of %95
n3=((1/n1)+(1/n2))
cresult=stats.t.interval(0.95,df=(n1+n2-2),loc=(maean1-mean2),scale=np.sqrt(n3*varab))
print(cresult)

