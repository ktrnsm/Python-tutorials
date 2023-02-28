#API uygulamanın başka bir uyguşamanın kullanması için gereken yapı, api servisi
# api servisi için api key ihtiyacı var, api için döküman verilmesi gerekiyor ki anlaşılır olsun.
import requests
import json

while True:

    lat=input("Please type the lat as sample as 25.4")
    lon=input("Please type the lon as sample as 25.4")
    apikey="0f2773a64cf57d97c3b01e7b79570977"
    address="https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&lang=tr&units=metic".format(lat,lon,apikey)
    connect=requests.get(address)

    surv=connect.json()
    # print(surv) bütün veriyi yazar

    weather=surv["weather"][0]["description"] # sadece havanın bulutlu açık vb tanımın aldık
    heat=surv["main"]["temp"]#sadece hava durumu bilgisi
    feltheat=surv["main"]["feels_like"]
    minheat=surv["main"]["temp_min"]
    maxheat=surv["main"]["temp_max"]

    print("{} coordinate the weather is as below\n\n Heat:{}°\nCondition:{}\nfeltheat{}°\nMinheat:{}\nMaxHeat{}\nHumidity:{}".format(lat,lon,weather,heat,feltheat,minheat,maxheat))