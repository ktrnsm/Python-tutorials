#91 NumPy-1st
import numpy as np
serial=np.array([1,2,3,4,5,6,7,8],dtype=int) 
#print(type(serial)) # tek boyutlu dizi

serial2nd=np.array([[1,2],[3,4],[5,6],[7,8]])
#print (type(serial2nd))

print(serial)
print(serial2nd)
print(serial2nd.shape)#dizinin boyutlarını yazar [4,2] dört adet iki elemanlı gibi
#array dizi oluşturur
#reshape ile matris tanımlanır.
serial3rd=serial.reshape(2,4)
print(serial3rd)

serial4th=np.array(["1","2",3,4,4.1,5])
print(serial4th.dtype)

serial5th=np.array([1,2,3,4,5,6,7,8],dtype=int)
serial6th=np.array([1,2,3,4,5,6,7,8],dtype=float)
serial7th=np.array([1,2,3,4,5,6,7,8],dtype=complex)
serial8th=np.array([1,2,3,4,5,6,7,8],dtype=str)
serial9th=np.array([1,2,3,4,5,6,7,8],dtype=bool) 




