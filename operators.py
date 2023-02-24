print(2+3)

print(3.5454+6.8587) # float olarak döndürür

print(5/3)
print(5//3) #tam sayı olarqak sonucu döndürür
print(5**3) # üzeri olarak verir
print(5%3) # sadece kalanı döndürür

#atama operatörleri

x,y=20,30
print(x,y)

x+=5 # x=x+5
x+=x+5 # 45 olarak döndürür
x*=5
x*=y
x/=10
x**=2
x//=2.5
x%=3

#karşılaştırma operatörleri

x,y=9,12
print(x<y) #False döndürür
print(x>y) # True döndürür

print(x==10) # x 12 olduğu için False döndürür
print(x!=10) # True olarak döndürür

x=[1,3,5]
print(3 in x) # yer alıyorsa True almıyorsa False olarak döndürür
x=[2]
y=[2]

print(id(x),id(y))  # id değerini yazdırır

print(x is y)# False döndü sebebi id'leri kontrol eder

print(x is not y) #True döndürür