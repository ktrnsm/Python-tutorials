#76
#connecting with request to a website
import json
import requests

site=requests.get("https://jsonplaceholder.typicode.com/todos")
#answer=site.text str olarak döner
answer=json.loads(site.text) # list olarak döner    
for i in answer:
    print(i["title"])
print(answer[0]["title"]) # listenin ilk elemanının özelliğine kadar çekebiliyoruz.

#print(type(answer)) 
#terminal [200] ulaşılabilir anlamındadır.



#print(json.__file__)
#pypi.org >> diğer kütüphanelere ulaşmak için
#pip install requests terimnale yazılır.