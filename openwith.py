with open("Trial.txt","a+",encoding="utf-8") as Folder:# utf-8 türkçe karakterleri tanıyor. "+" hem okuma hem yazma işlemi yapıyor.
    print(Folder.read())
    Folder.seek(15) # 15. karakterden sonra aşağıda yazılanı ekler.
    Folder.write("\n hi there")
    print(Folder.read() # seek olmazsa yazılan son karakterden okumaya başladığ için boş döner.)


    Folder.seek(9) # 9 karaterden sonrasını okumaya başladı.
    print(Folder.tell())# hangi karakterde kaldığını gösterir.
    print(Folder.read(15)) # 15 karakter okuyor.


    
