from twython import Twython
import json
from pymongo import MongoClient
import datetime
import time

TimerStart = datetime.datetime.now()
TimerEnd = TimerStart + datetime.timedelta(hours = 1)

# mongoDB Host
MONGO_HOST = 'mongodb://127.0.0.1/'
client = MongoClient(MONGO_HOST)
database = client.Twitter

# The tracking tag list
Glasgow = [55.8714, -4.2885, "63mi"]

# Developer key and token
# Consumer API keys
API_Key = "API KEY HERE"
API_Secret = "API SECRET HERE"

# Access token & access token secret
Access_Token = "ACCESS TOKEN HERE"
Access_Secret = "ACCESS SECRET HERE"

def store(tweet):
    # Setup mongoDB Host to Localhost and point to a database
    datajson = json.loads(json.dumps(tweet))
    database.RESTGEOTag.insert(datajson)

if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    API = Twython(API_Key, API_Secret)
    count = 0
    iteration = 1
    print("REST API Set up")
    print("Tracking " + TRACK)
    print("Start Collecting")

    iteration = 0

    while datetime.datetime.now() < TimerEnd:
        # Start collecting data
        # In the first iteration 0, it will return a next max id
        # max id tells the API from where the data is returned in the next iteration
        # After the first iteration, max_id can be passed to GET operation
        # Only extract those posts written in English and located in the selected location
        try:
            if(iteration == 0):
                tweets = API.search(geocode = Glasgow, count='100', lang = "en")
                iteration+=1
            else:
                tweets = API.search(geocode = Glasgow, count='100', max_id=nextMaxId, lang = "en")
                iteration+=1

            for tweet in tweets['statuses']:
                count+=1;
                store(tweet)
        except twython.exceptions.TwythonRateLimitError:
            print("Rate limit exceeded, wait for 15 minutes")
            time.sleep(900)

        # The next max id is in the tweets' result
        try:
            # Pass the max id to next iteration
            nextResult = tweets['search_metadata']['next_results']
            nextMaxId = nextResult.split('max_id=')[1].split('&')[0]
        except:
            # No more next pages
            print("No More pages, Programme stop")
            break

    if(datetime.datetime.now() > TimerEnd):
        print("1 Hour Reach, Programme stop")
    print ("Execution Time: " + str(datetime.datetime.now() - TimerStart))
