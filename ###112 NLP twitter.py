###112 NLP twitter
import snscrape.modules.twitter as sntwitter
import pandas as pd
from itertools import islice

df=pd.DataFrame(islice(sntwitter.TwitterSearchScraper("NLP").get_items(),1))
#print(df.columns)

data=sntwitter.TwitterSearchScraper("NLP").get_items()

twit_list=[]
for i in data:
    if len(twit_list)==50:
        break
    else:
        twit_list.append([i.url,i.date,i.content])
#print(i.date)
#print(i.content)
#print(twit_list)

df=pd.DataFrame(twit_list,columns=["url","Date","Twits"])
print(df)

