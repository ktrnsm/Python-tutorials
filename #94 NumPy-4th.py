#94 NumPy-4th
import numpy as np
#x=np.arange(16).reshape(4,4)
#print(x)
#y=np.delete(x,[0],axis=0)#0' satırı komple kaldırdı
#z=np.delete(x,[0],axis=1) # stün bazlı komple silme
#k=np.append(x,[[45],[49],[69],[12]],axis=0)# satır bazlı ekleme
#l=np.append(x,[[45],[49],[69],[15]],axis=1)# satır bazlı ekleme

#print(y)
#print(z)
#print(k)


a=np.array([8,6,2,5,2])
b=np.array([1,8,9,2,4,4])

print(np.setdiff1d(a,b)) # xte olup y'de olmayan elemanları verir
print(np.union1d(a,b)) # birleşim kümesi
print(np.in1d(a,b)) # aynı eleman varsa true yoksa false olarak döndürüyor.
print(np.unique(a)) #tekrardan arındırılmış olarak döndürür.
print(np.sort(a)) # küçükten büyüğe sıralama yapar.
