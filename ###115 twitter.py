###115 twitter
import pandas as pd
import re
from textblob import TextBlob
import matplotlib.pyplot as plt 

original_data=pd.read_csv("C:/Users/ŞEbnem/Desktop/tutorials/tweets.csv")
data=original_data.copy()

def cleared_data(tweet):
    tweet=re.sub('#[a-zA-Z0-9]+'," ",tweet)
    tweet=re.sub('\\n'," ",tweet)
    tweet=re.sub('@[\S]*'," ",tweet)
    tweet=re.sub('https?:\/\/\S+'," ",tweet)
    tweet=tweet.lower()
    tweet=re.sub('[^a-zA-Z0-9]+'," ",tweet)
    tweet=re.sub('^[\s]+|[\s]$'," ",tweet)
    return tweet

data["cleared data"]=data["Tweets"].apply(cleared_data)

data2nd=data.loc[0:500,:].copy()

def sent_score(tweet):
    blob=TextBlob(tweet)
    return blob.sentiment.polarity

data2nd["Sent Score"]=data2nd["Tweets"].apply(sent_score)

def sent_situation(situa):
    if situa<0.0:
        return "Negative"
    elif situa>0.0:
        return "Positive"
    else:
        return "Notr"

data2nd["Sent situa"]=data2nd["Sent Score"].apply(sent_situation)

data2nd["Sent situa"].value_counts().plot(kind="bar")
plt.show()
print(data2nd)