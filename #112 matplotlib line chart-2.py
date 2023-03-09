import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.title("Sample chart")
plt.xlabel("Year")
plt.ylabel("Qty")
Year=[17,18,19,20,21,22,23]
s1st=[10,8,8,45,78,19,5]
s2nd=np.sqrt(s1st)
plt.plot(Year,s1st,color="red",linewidth=3,marker="x",ms=15,mec="blue",mfc="yellow",linestyle="dotted",label="s1st")
# s,d farklı işaretleme değerlerni veriyor. ms işaretçinin büyükllüğünü belirtiyor
#mec dış çizgi, mfc işaretçinin kendisini belirtiyor.
#doted veya : kesik çizgi şeklinde çiziyor. dashed daha uzun kesikli çizgi
#dash çizgi nokta çizgi -. # solid orijinal ifadeye dönüyor.
plt.plot(Year,s2nd,color="green",linewidth=2,label="s2nd")
plt.legend(loc=9) # çizginin etiketini ekliyor. loc girmezsek sol üste yazıyor.
plt.grid(axis="x") # grid yapısına dönüştürüyor. sadece x üzerinden yap 
plt.show()


