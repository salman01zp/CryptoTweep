import tweepy
from time import sleep
from credential import *
import json
from tweepy import StreamListener
from tweepy import Stream


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class StdOutListener(StreamListener):

    def on_data(self, data):
    	# print(data)
    	
          
    	feed_dict = json.loads(data)
    	
    	if "text" in feed_dict:
    		print ("{0[user][name]}: {0[text]}".format(feed_dict))

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    listener = StdOutListener()
    twitterStream = Stream(auth, listener)
    # friends = api.friends_ids()
    # ids = list(map(str, friends))

    users = ['706134862076313601','890621967627419648']
    twitterStream.filter(follow= users )
