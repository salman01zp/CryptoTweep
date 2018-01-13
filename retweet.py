import tweepy
from time import sleep
from credential import *

auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token , access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, lang ='fr',q = '').items(100)
	try:

		print('Tweet by: @' + tweet.user.screen_name)
	except tweepy.tweepError as e:
		print(e.reason)

	except StopIteration:
		break
		
