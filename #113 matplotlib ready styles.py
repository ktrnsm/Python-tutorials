#113 matplotlib ready styles
import matplotlib.pyplot as plt
print(plt.style.available) # hazır stiller

plt.style.use("seaborn-v0_8-colorblind")

for i in plt.style.available:
    print(i)

x=[18,19,20,21,22]
y=[10,15,20,45,35]
plt.plot(x,y)
plt.show()
