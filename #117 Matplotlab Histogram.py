#117 Matplotlab Histogram
import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(1000)
x1=np.random.normal(0,1,1000)
x2=np.random.normal(-5,0.7,1000)
plt.hist(x,alpha=0.5)
plt.hist(x1,alpha=0.5)
plt.hist(x2,alpha=0.5)
middle=np.median(x)

plt.hist(x, color="red",edgecolor="black",histtype="bar",rwidth=1)#adımlama stepfilled
plt.axvline(middle,color="blue")
plt.show()
