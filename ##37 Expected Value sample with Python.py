##37 Expected Value sample with Python
from scipy import stats
from scipy import integrate

x=[1,2,3,4,5,6]
p=[1/6,1/6,1/6,1/6,1/6,1/6]
expected=stats.rv_discrete(values=([x],[p])).expect()
print(expected)

def f(x):
    return 3/7*x**3 # bu return ifadesi olmak zorunda ki f(x)'a atama yapsın.

expectedvalue=integrate.quad(f,1,2)
print(expectedvalue)
#(1.6071428571428572, 1.7842870038618588e-14) ilk kısım sonuç ikinci kısım integralin güvenilirliği

