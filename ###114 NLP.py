###114 NLP
import pandas as pd
from textblob import TextBlob

text= ["My name is red", "Mien name is Rot", "benim adim kirmizi"]

for i in text:
    blob=TextBlob(i)
    ingblob=blob.translate(to="en")
    print(ingblob.sentiment)

original_data=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/tweets2nd.csv")
data=original_data.copy()

#print(data)