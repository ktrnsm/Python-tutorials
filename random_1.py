import random

x=random.random() # 
print(x)

x=random.randint(1,1000)
print(x)

y=["a","b","ci","d"]
x=random.choice(y)
print(x)

List=range(0,100)
x=random.sample(List,20)
print(x)