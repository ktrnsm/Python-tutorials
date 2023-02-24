#metotlar
#sayısallar
x=-2.7
print(x.__abs__())  #abs mutlak değer döndürür

print(pow(x,3)) #üçüncü kuvvetini aldı

print(x.__divmod__(2)) # 15/2 işleminde kalan ve bölümü verir

print(x.as_integer_ratio()) #x değerini elde etmek için hangi sayının hangi sayıya bölünmes gerektiğini veriyor.

print(x.is_integer()) # integer olup olmadığını kontrol edip bool değer döndürüyor

#string metodlar

#w3 school da python metotların listesi ve detayları mevcut

x= "anlaşılır ekonomi"
print(type(x))

y=x.lower()
y=x.upper()
y=x.islower() #true false döndürür
y=x.isnumeric() #sayısal oup olmadığına bakar
y=x.isalnum() # harf ve rakam dışında karaktere bakar bool döndürür
y=x.capitalize() #ilk harf büyür
y=x.title() # kelime baş harflerini büyütür
y=x.swapcase() # büyük küçüğü ters çevrir
y=x.count("a") # yazılan değerin adını değerlendirir.
y=x.strip(" ") #fazla boşlukları temizler A koyarsak A'ları siler
y=x.lstrip("ek") # soldan başlar ve siler
y=x.split(" ") # virgülle boşluklar arasını parçalar 
y=" ".join(y) # split'in tersini yapar.
y=x.find("ko") #arananın index numarasını verir. bulamazsa -1 döndürür.
y=x.replace("ko","ok") # ilk yazılan ile ikincisini değiştirir.


Adı="Anlaşılır"
Soyadı="Ekonomi"
Görevi= "Eğitmen"

Bilgiler=[Adı,Soyadı,Görevi]

print("Kişinin Adı{}, Kişinin Soyadı{} Kişinin Görevi{}".format(Bilgiler[0],Bilgiler[1],Bilgiler[2]))

#liste metotları
List=[1,2,5,"Merhaba",2.5]
List.append("Anlaşılır Ekonomi") #sonuna ekleme yapar)
List.insert(3,"ktrn") #ilk yazılan indexi değiştirir.
List.pow() # son sıradaki datayı siler 2. index girersek o indexi siler
List2=List.copy()
List.extend(List2) # ikinci listeyi ekler
List+=List2 # aynısı yapacaktır

List.count(3)# kaç adet olduğunu döndürür

List.sort() # kğçükten büyüğe sırala
List.sort(reverse=True) # tersten sıralar
List.reverse() # sondan başa listeler indexilier tersine çevrir.
List.clear() # listeyi temizler

#demet metotları
x=(1,"Merhaba",2.5)
print(x.index(2,5)) # index noyu verir
print(x.count(1))# kaç adet olduğunu sıralar.


#sözlük metotu

Bilgi={
    "Ad":"ktrn",
    "Soyad":"sm",
    "Dyer":"ÇAnkıtı",
    "TVK":123456123

}
print(type(Bilgi.keys)) 
print(Bilgi.items) #anahtar ve eşleşmeleri gösterir
Bilgi.get("Ad") # anlaşışırı döndürür
Bilgi.update({"Cinsiyet":"Erkek"}) # sözlük üzerinde güncelleme
Bilgi2=Bilgi.copy()

print(Bilgi.__len__())
Bilgi.pop("TVK") # anahtarı siler
Bilgi.clear() # komple siler

#küme metotları

Küme={1,2,"ktrn",2.5}
Küme.add(3.4)
Küme.discard("ktrn") #hata döndürmez ama .remove hata döndürür.