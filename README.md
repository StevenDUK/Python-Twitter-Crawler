#Twitter Crawlers

## MongoDB
Before run this product, please ensure the machine has mongoDB installed.

### Install
```
brew install mongodb
```

### Run Server in Localhost
```
mongod
```

### Run MongoDB Shell
This allows terminal to run MongoDB on localhost:27017

```
mongo --host 127.0.0.1:27017
```

## Library
These are the libraries should be installed via ```pip``` in this series of programmes:

* pymongo
* twython
* tweepy

## Collecting Data
This programme will execute all the crawlers including:

* StreamingAPI_1%.py
* StreamingAPI_Topic.py
* RESTAPI_Keyword.py
* StreamingAPI_GeoTag.py
* RESTAPI_GeoTag.py
* redditAPI.py

```
python Crawler.py
```

**WARNING:** The programme will clean the database to ensure the databases that the crawlers are creating are empty.

**WARNING:** The programme is estimated to finish in 4 hours.