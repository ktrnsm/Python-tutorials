#92 Numpy-2nd
import numpy as np
zero=np.zeros((5,5),dtype=int)
one=np.ones((3,4),dtype=int)
first=np.full((5,5),20,dtype=int)
#print(first)
#print (one)
#print(zero)

second=np.eye(5)
print(second)

third=np.diag([1,2,3,4,5])
print(third)

forth=np.arange(0,100,5)# 100'e kadar 5'er atlayarak devam ediyor.
print(forth)

fifth=np.linspace(0,100,5)# 1-0-100 varasını 20'şer böler
print(fifth)
sixth=np.random.rand(3,4)
print(sixth)

sixth=np.random.randint(0,10,size=(5,5)) # 0-10 arasında random sayılardan 5'e5 matris oluşturmak
print(sixth)

seventh=np.random.randn(3,4)#
print(seventh)