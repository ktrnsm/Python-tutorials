###114 alternative

import tweepy

# authenticate with your Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# create a Tweepy API object
api = tweepy.API(auth)

# search for tweets containing "xxx"
search_query = "bitcoin"
tweets = api.search(q=search_query, lang="en", count=10)

# print the tweet texts
for tweet in tweets:
    print(tweet.text)
