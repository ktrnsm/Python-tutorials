###113 nlp via twitter
import snscrape.modules.twitter as sntwitter
import pandas as pd

data=sntwitter.TwitterSearchScraper("My name is Red").get_items

twit_list=[]

for i in data:
    if len(twit_list)==50:
        break
    else:
        twit_list.append(i.content)

df=pd.DataFrame(twit_list,columns="Twits")
print(df)