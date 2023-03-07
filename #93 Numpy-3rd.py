#93 Numpy-3rd
import numpy as np

x=np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
print(x[0])#0. indexi yazdırır
print(x[-1]) #son değeri döndürür
print(x[::]) #tamamını düz yazdırır
print(x[::-1]) # terstedn döndürür

#for i in x:
#    print(i)

print(x[3,0]) # 3. index 0. eleman
print(x[:,0]) # ilk stünu getirir. index parametresini ayırdık.
print(x[:,1]) #ikinci stünu getirir.

