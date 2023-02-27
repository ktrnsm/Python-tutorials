#folder management
#w mod write eski dosyayı kaldırır aynısı varsa
#r mod read
#a mod add mevcut dosyaya yazılan karakteri ekler
#x mod dosya mevcutsa hata döndürür

#Folder=open("C:/Users/Şebnem/Desktop/tutorials/hi.txt","w")
#Folder.write(" hi there my name is red")
#Folder.close() # dosyanın açıldıkta sonra kapatılması gerekiyor.

Folder=open("hi.txt","a")
Folder.write("\n my name is red")
Folder.close()

#Folder2=open("trial.txt","a")
#Folder2.write("\nhi my name is red and what is your name")
#Folder2.close()

Folder=open("trial.txt","r")
print(Folder.read())

print(Folder.readline())# dosya açık olduğu sürece tek tek satırları okur.

print(Folder.readlines()) # liste olarak oluşturur

List=Folder.readlines()
print(List[2]) # serini üçüncü karakterini yazar

print(Folder.read(4))# ilk 4 karakteri döndürür

for i in Folder:
    print(i,end="") #boşluk bırakmadan satır atlamadan yazdırma
Folder.close()

