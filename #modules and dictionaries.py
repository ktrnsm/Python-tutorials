import math # math ifadesini kullanmak gerekir.
from math import* # tamamnı indirir math ifadesini kullanmak gerekmez

from math import sqrt # kullanılan tanımlanıyor ve kendisi ekliyor.
#modules and dictionaries
x=pow(2,3)
print(x) 

def squareroot(x):
    result=x**0.5
    print(result)

squareroot(4)

x=help(math)
print(x)

x=math.pi
x=math.sqrt(25)
x=math.factorial(49)
x=math.floor(9.5) # aşağı yuvarlar
x=math.ceil(9.5) # yukarı yuvarlar