#95 NumPy-5th
import numpy as np
x=np.array([8,6,4,5,2])
y=np.array([1,5,6,8,7])

print(x*y)
print(x/y)

print(np.add(x,y)) # fonksiyon olarak toplama
print(np.subtract(x,y))
print(np.divide(x,y))
print(np.multiply(x,y))
print(np.min(x)) # minimmum değer
print(np.max(y)) # min değer
print(np.sqrt(x))
print(np.log(x))
print(np.sum(x)) # x değerlerini toplar
print(np.mean(x)) # ortama
print(np.median(x))
print(np.std(x))
print(np.sqrt(np.var(x)))