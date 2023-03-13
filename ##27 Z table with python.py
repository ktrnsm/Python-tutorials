##27 Z table with python

#Sample 1
#mean =5.3
#std=1
#P(x>45)
from scipy.stats import norm
pos1st=1-norm(loc=5,scale=1).cdf(4.5)
print(pos1st)


#Sample 2
#P(45<x<65)
highborder=norm(loc=5.3,scale=1).cdf(6.5)
lowborder=norm(loc=5.3,scale=1).cdf(4.5)
poss3rd=highborder-lowborder
print(poss3rd)

#Sample 3
#mean=60
#std=12
#P(60<x<70)
highb=norm(loc=60,scale=12).cdf(60)
lowb=norm(loc=60,scale=12).cdf(45)
poss4th=highborder-lowborder
print(poss4th)

#P(x<45)
lowb=norm(loc=60,scale=12).cdf(45)
print(lowb)


#Sample 4
#mean=800
#std=40

#P(778<x)
p=norm(loc=800,scale=40).cdf(778)
print(1-p)

#P(x<834)
p2=norm(loc=800,scale=40).cdf(834)
print(p2)
