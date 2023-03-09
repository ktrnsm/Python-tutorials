#103 Pandas Data framework data gruoping
import pandas as pd
data=pd.DataFrame(pd.read_excel("C:/Users/Şebnem/Desktop/tutorials/hastane.xlsx"))
Male=data.groupby("Cinsiyet").get_group("Erkek")["Cinsiyet"].count()
Female=data.groupby("Cinsiyet").get_group("Kadın")["Cinsiyet"].count()
print(Male)
print(Female)

print(f"Male ill rate %{(Male/(Male+Female))*100},\n Female il rate{(Female/(Male+Female))*100}")

#age average of the ills

#ageav=data["Yas"].mean()
#print(ageav)

data2=pd.DataFrame(pd.read_excel("C:/Users/Şebnem/Desktop/tutorials/hastane.xlsx"))
averageage=data2.groupby("Cinsiyet")["Yas"].mean()
print(averageage)
averageagebyCity=data2.groupby(["Cinsiyet","İl","İlce"])["Yas"].mean()
print(averageagebyCity)
