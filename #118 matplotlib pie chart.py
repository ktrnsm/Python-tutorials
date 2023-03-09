#118 matplotlib round chart
import matplotlib.pyplot as plt
autos=["a","b","c","d"]
price=[10,20,50,80]
x=[35,15,25,15]
distance=[0.2,0,0.4,0]
colours=["red","yellow","pink","blue"]
plt.pie(price,labels=autos,startangle=90,explode=distance,shadow=True,colors=colours, autopct="%1.1f%%")
#%'lik oranları da yazılı olarak belirtir.

plt.show()