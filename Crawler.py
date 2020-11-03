##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Created by: Yao-I Tseng
## Email: mrsuccess1203@gmail.com
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

from pymongo import MongoClient
import datetime

TimerStart = datetime.datetime.now()

# Setup mongoDB Host to Localhost and point to a database
MONGO_HOST = 'mongodb://127.0.0.1/'

# There the table are created
client = MongoClient(MONGO_HOST)
database = client.Twitter
database.command('dropDatabase')

# Each API is packed as a individual file
# To run a specific API, remove other APIs from below
print("Starting 1% Streaming API")
exec(open("./StreamingAPI_1percent.py").read())
print("---------------------------")

print("Starting Topic Base Streaming API")
exec(open("./StreamingAPI_Topic.py").read())
print("---------------------------")

print("Starting Keyword Base REST API")
exec(open("./RESTAPI_Keyword.py").read())
print("---------------------------")

print("Starting GeoTag Streaming API")
exec(open("./StreamingAPI_GeoTag.py").read())
print("---------------------------")

print("Starting GeoTag REST API")
exec(open("./RESTAPI_GeoTag.py").read())
print("---------------------------")

print ("Execution Time: " + str(datetime.datetime.now() - TimerStart))
