#114 matplotlib scatter
import matplotlib.pyplot as plt
import numpy as np
cs=[1.75,1.5,0.5,3,3.25,2]
point=[17,15,7,19,20,12]
plt.title("point distbution")
plt.xlabel("hour")
plt.ylabel("point")
plt.axis(0,4,0,20)
colours=np.random.randint(0,100,6)
plt.scatter(cs,point,s=300,c=colours,cmap="reds",marker="+",edgecolors="black",alpha=0.5) # noktalar büyütülebilir.
plt.colorbar()# renk skalası koyuyor.
plt.show()