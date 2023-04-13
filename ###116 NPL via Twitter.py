###116 NPL via Twitter
import pandas as pd
import re
from googletrans import Translator,LANGUAGES
from time import sleep
original_data = pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/tweets2nd.csv")
data = original_data.copy()

def clarify(tweet):
    tweet = re.sub('#[a-zA-ZÇŞİĞÜçöişğü0-9]+', " ", tweet)
    tweet = re.sub('\n', " ", tweet)
    tweet = re.sub('@\w+', " ", tweet)
    tweet = re.sub('https?:\/\/\S+', " ", tweet)
    tweet = tweet.lower()
    tweet = re.sub('^[a-zA-ZÇŞİĞÜçöişğü0-9]', " ", tweet)
    tweet = re.sub('^[\s]+|[\s]+$', " ", tweet)

    return tweet

data["Tweets"] = data["Tweets"].apply(clarify)
#print(data)

translate = Translator()
def trans(tweet):
    try:
        t=Translator()
        result=t.translate(tweet,src="tr",dest="en")
        sleep(0.5)
        return result.text
    except TypeError:
        return "failure"

data2nd=["Translate"]