##26 z table sample
#job interview
##test score
#mean=60
#std=12
#disturbition as normal dis.

##1 random selected candity the 60-70 score rate possibility
##2 45-60 possibility
##3 lower than 45 possibility


###1 Solution
#P(60<x<70)
meanvalue=60
stdvalue=12
z1=60-meanvalue
z2=70-meanvalue
z3=(z2-z1)/stdvalue
print(z1)
print(z2)
print(z3)
## z table z3>>0.83 ====0.2967

###2 Solution
#p(45<x<60)
#45-mean/stdvalue  >>-1.25
#z table 1.25>>0.3944

###3 Solution
#P(x<45)0.5-0.3944 ===0.1056


#producted light
Meanvalue=800
stdvalue=40

#dist is normal.

#1 more than 778 hours
#P(x>778)
z1=(778-800)/40 #>>-0.55 0.21

#2 less than 834 hours
#P(x<834)
z1=(800-834)/40 #>>0.85  0.30  0.5+0.3 >> %80

#3 between 778,834
#P(778<x<834)
z1=(778-800)/40 #>>0.55  %21
z2=(778-834)/40 #>>0.85 %%30 
#%51


#products diameter mean =3.005 std=0.001  if 3.000+-0.002 is
# production failure
#find the failure rate
meanvalue=3.0005
stdvalue=0.001
#istborder=2.998<x<3.002
z1=(2.998-meanvalue)/stdvalue #-2.5 >> %49
z2=(3.002-meanvalue)/stdvalue #-1.5 >> %43
#witout failure %92
# failure %8 
