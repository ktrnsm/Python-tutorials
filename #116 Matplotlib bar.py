#116 Matplotlib bar
import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
chart=fig.add_axes([0.1,0.1,0.8,0.6])
#cars=["a","b","c","d"]
#prices=[5,7,9,2]
#chart.bar(cars,prices,color="red",width=0.2,label="Average Price")
#chart.barh(cars,prices,color="red",height=0.2,label="Average Price") yatay oluşturma

#chart.set_title("Price Bar Chart")
#chart.legend()
#plt.show()
classes=["A","B","C","D","E"]
index=np.arange(len(classes))
a=0.25
Math=[90,55,75,45,35]
Gram=[80,50,60,45,89]
ph=[40,35,20,10,12]

chart.bar(index-a,Math,label="Math",color="red",width=a)
chart.bar(index,Gram,label="Grammar", color="blue",width=a)
chart.bar(index+a,ph,label="Physics",color="green",width=a)
chart.set_title(" average notes of classes",color="black")
chart.set_xlabel("Classes")
chart.legend()
chart.set_xticks(ticks=index,labels=classes)
plt.show()