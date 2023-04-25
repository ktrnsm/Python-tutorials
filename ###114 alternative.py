###114 alternative

import tweepy
##bearer token AAAAAAAAAAAAAAAAAAAAALP0mwEAAAAAq%2FXezswvYPOPdDPSHUSIakQgePM%3DtiV7jKctq0LkFtNLYJmdO0Gk75wDDptM7aLtCdTl6cg7lAUzLk
# Access token 1051548702832295936-sGNrvShaxH8mXYbzB8gJjPP8joZFS8
 #access token secret 3FuUsdZ42KGqOIxYt9jlp5JZAcNpOySQIaC1j0PlvswB1
 
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
tweets = tweepy.Cursor(api.search_tweets,
                       q=search_query,
                       lang="en",
                       tweet_mode='extended').items(10)

# print the tweet texts
for tweet in tweets:
    print(tweet.full_text)
