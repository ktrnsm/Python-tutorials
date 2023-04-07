###101 NLP_1
import pdfplumber
import pandas as pd
with pdfplumber.open("C:/Users/Şebnem/Desktop/tutorials/my_name_is_red.pdf") as pdf:
    page = pdf.pages[0]
    text = page.extract_text()
text=text.replace("!",".")
#print(text) 
d1=text.split(".")
d2=[]
for i in d1:
    d2.append(i.replace("\n","").strip(" "))
#print(d2)

df=pd.DataFrame(d2,columns=["Sentences"])
print(df)