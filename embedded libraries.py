print(abs(-5)) # mutlak değer alma fonksiyonu
print(round(22/7,3))# en yakın tam sayıya yuvarlar virgülden sonraki değer kaç rakam olduğunu belirtir.
x=[3<4,3<5,6<3]
print(all(x)) # tamamı true ise true 1 hata varsa false döndürür
print(any(x))#tek true varsa true döndürür.

print(ascii("\n"))
print(bool(0))
print(chr(25)) # karakterin sayı karşılığı

x=list() 
x.append(1)
print(x)
z=list(x)
print(z)# indexler ve str olarak yazar

x=set()
print(type(x))# küme olduğu bilgisini döner
y=set(x)
print(y) # listeyi kümeye dönüştürür kümede aynı karakterler bulunmaz.

dict # kütüphane oluşturma için kullanılır
print(float(2))
Age=int(input("enter your age please"))

print(dir.list) # listin kendisine ait fonksiyonları görmemizi sağlar

print(divmod(15,5)) #tam ve kalan kısmını yan yana yazıyor

x="ktrn sm"
print(*enumerate(x)) # str içinde her karakterin index nosunu ekliyor.

help(dir) # dir fonksiyonunun ne işe yaradığnı veriyor

x=2
y="2"
print(id(x)) # id numaraları ile saklanıyor sistemde
print(id(y))

int(input()) # input str alır farklı istenirse çevrilmesi gerekir

x="ktrn sm"
y=["ktrn sm"]
print(len(x)) # seri olmadığı içn bir verir y karakter adedini verir.
print(len(y))

x=["A","AB","C"]
print(max(x,key=len)) # maksimum uzunluk aradığımız için onu veriyor.
print(min(x,key=len()))

#print
print("ktrn", "sm", "smh",sep="---", end="...") # aralarına seperatör koyuyor sonuna koyuyor.

print(range(0,100)) #yapıyı yazdırır
print(list(range(0,100))) #100'e kadar 100 hariç tek tek yazdırır

x=["A","B","C",12]
print(list(reversed(x))) # tersini yazdırır


print(type(x))

x=[1,2,3,4]
y=["A","B","C","D"]

print(*zip(x,y)) # yıldız eklendiğinde eşleştirerek yazar
