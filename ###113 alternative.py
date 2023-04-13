###113 alternative
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Specify the search query correctly
data = sntwitter.TwitterSearchScraper('"My name is Red"').get_items()
data2 = sntwitter.TwitterSearchScraper("from:mynameisred").get_items()
data3 = sntwitter.TwitterSearchScraper("to:mynameisred").get_items()
data4 = sntwitter.TwitterSearchScraper("from:mynameisred to:mynameisred").get_items()
data5 = sntwitter.TwitterSearchScraper("from: mynameisred since:2023-04-12 until:2023-04-13").get_items()
data6 = sntwitter.TwitterSearchScraper("mynameisred min_faves:10000").get_items()
data7 = sntwitter.TwitterSearchScraper("mynameisred min_retweet:10000").get_items()
data8 = sntwitter.TwitterSearchScraper("mynameisred near:10000").get_items()

tweet_list = []

for i, tweet in enumerate(data):
    # Use i + 1 instead of len(twit_list) to count the number of tweets
    if i + 1 > 50:
        break
    else:
        tweet_list.append(tweet.content)

# Specify the column name as a list
df = pd.DataFrame(tweet_list, columns=['Twits'])
print(df)
