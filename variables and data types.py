x=2+3j
print (type(x)) # tipi gösterir
print ("HEllo world")


 #string veri tipleri

x= "ktrn semih"
y="aga"
print (x[-2])
print(x[0:6:2]) # 0-6 karakter arasında 2şer atlayarak git
print(x,y)
print(x+" "+"\n"+y) # alt satıra geçerek devam et

print(len(x))

print(x[len(x)-1]) # son karakteri yazdır

#bool
print(10>5) # true olarak değer döndürür

x=True
print (type(x))

# Liste yapısı
knowledge=["Sen","Ben","O"]
print(knowledge)
print(knowledge[1])
x="Ahmet"
print(x[2])
knowledge[0]="Biz"
knowledge2=["Biz","Siz","Onlar"]
knowledge3= [knowledge+knowledge2] #iki seri birleştiriliyor
print(len(knowledge3)) # bu listenin uzunluğu ikidir.

Ürünler=["tv","rad","bil","fırın"]
print(len(Ürünler))

print(Ürünler[0:2]) #ilk üç elemanı listele)

print(Ürünler[0],Ürünler[len(Ürünler)-1])

Ürünler[len(Ürünler)-1]="Ütü" #değiştirme işlemi

Ürünler=Ürünler+["Çamaşır makinesi"] # listeye eleman eklenmesi

#Tersten yazdırma

print(Ürünler[::]) #tamamını yazdırma kısa yolu
print(Ürünler[::-1]) #tamamını tersten yazdırma

#sözlük veritipi / dictionary anahtar yapısı

Kimlik={"İsim":"Ahmet",    "Soyisim":"Doğu",    "Yaş":41,    "D.Yeri":"Ankara"}
print(Kimlik["İsim"])

#yeni key ve içeriğini ekleme
Kimlik["İsim"]="Mehmet"
Kimlik["TCK"]=123456789123
print (Kimlik)

kullanicilar={
"Ahmetcan":{
    "TCK":1234567,
    "D.Yer":"angara",
    "Yaş":24
},
"Arzucan":{
    "TCK":1234567,
    "D.Yer":"angara",
    "Yaş":24

}
}
print(kullanicilar["Ahmetcan"])

#Demet Yapısı değişiklik yapılamaz, listelere göre daha hızlıdır

liste=["Ahmet",23]
print(type(liste))

demet1=("Ahmet")

demet2=("Ahmet",23) #demet tuple yapısı değiştirilemezler

#Kümeler indexlenemez, tekrarlı veri barındırmaz

kume={"Ahmet",9,"Ahmet"}
print(kume) # tek ahmet döndürür, metotlar dışında değişiklik yapılamaması

#veri tipi dönüştürme
a=2
b=2.6
c="24"

d=str(a) # a str'ye dönüştürüldü
e=float(c) #
x=[1,3,5,7,9]
print(type(x)) #liste

y=tuple(x) # tuple/demet

z=set(x)  #küme yapısına dönüştürüldü

#fonksiyonlar
x=input("ilk sayıyı giriniz")
y=input("ikinci değişkeni giriniz")
z=x+y
print(z) #sorudan dolayı str olarak toplar
z= float(x)+float(y) # girdileri folat olarak oluşturur

print("Sonuç"+ " "+str(z))

çap=input("dairenin çapını giriniz")
yariçap= float(çap)/2
Pi=3.14
Alan=Pi*(yariçap*yariçap)
print("Dairenin Alanı"," ", str(Alan))


x="Merhaba"
print(x.index("r")) # 2 olarak yazacaktır index değerini belirtecektir.

print (dir(str))

 