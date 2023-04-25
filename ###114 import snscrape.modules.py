import snscrape.modules.twitter as sntwitter
import pandas as pd
tweet_list=[]
data=sntwitter.TwitterSearchScraper("Bitcoin lang:en").get_items()

for i in data:
    if len(tweet_list)==4:
        break
    else:
        tweet_list.append([i.date,i.content])

df=pd.DataFrame(tweet_list,columns=["Dates","Tweets"])
date_correction=df.select_dtypes(include=['datetime64[ns, UTC]']).columns

for i in date_correction:
    df[i]=df[i].dt.date

print(df)