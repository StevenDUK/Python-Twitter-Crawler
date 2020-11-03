import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from pymongo import MongoClient
import datetime

# Setup mongoDB Host to Localhost and point to a database
MONGO_HOST = 'mongodb://127.0.0.1/'
client = MongoClient(MONGO_HOST)
database = client.Twitter

# Developer key and token
# Consumer API keys
API_Key = "API KEY HERE"
API_Secret = "API SECRET HERE"

# Access token & access token secret
Access_Token = "ACCESS TOKEN HERE"
Access_Secret = "ACCESS SECRET HERE"

TimerStart = datetime.datetime.now()
TimerEnd = TimerStart + datetime.timedelta(hours = 1)

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):

        try:
            # Handle database connection
            datajson = json.loads(data)
            database.onePercent.insert(datajson)

            if datetime.datetime.now() > TimerEnd:
                raise Exception()
        except Exception:
            stream.disconnect()
            print("1 Hour Reach, Programme stop")
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    listener = StdOutListener()
    OAuth = OAuthHandler(API_Key, API_Secret)
    OAuth.set_access_token(Access_Token, Access_Secret)
    stream = Stream(OAuth, listener)

    print("Listener Set up")
    print("Collecting All Data.")
    print("Start Collecting")

    # Launch streaming API
    # Only extract those posts written in English
    stream.sample(languages=["en"])
    print ("Execution Time: " + str(datetime.datetime.now() - TimerStart))
