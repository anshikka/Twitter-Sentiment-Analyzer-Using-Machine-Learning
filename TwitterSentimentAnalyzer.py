import tweepy
from textblob import TextBlob

consumer_key = 'INSERT_CONSUMER_KEY_HERE'
consumer_secret = 'INSERT_CONSUMER_SECRET_HERE'

access_token = 	'INSERT_ACCESS_TOKEN_HERE'
access_token_secret = 'INSERT_ACCESS_TOKEN_SECRET_HERE'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('INSERT_SEARCH_QUERY_HERE')

#for sentiment analysis:
#polarity: Measures how positive or negative the text is
#subjectivity: Opinion vs Factual

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)




