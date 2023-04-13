###114 npl twitter
import snscrape.modules.twitter as sntwitter
import pandas as pd

tweet_list = []

data = sntwitter.TwitterSearchScraper('"My Name is Red"').get_items()

for i in data:
    if len(tweet_list)==1000:
        break
    else:
        tweet_list.append([i.date, i.rawContent])

df = pd.DataFrame(tweet_list, columns=["Dates", "Tweets"])
date_correction = df.select_dtypes(include=['datetime64[ns, UTC]']).columns

for i in date_correction:
    df[i] = df[i].dt.date

df.to_csv("c:/Users/Şebnem/Desktop/tutorials/tweets2nd.csv",index=False)
