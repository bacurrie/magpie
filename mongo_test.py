import pymongo
from pymongo import MongoClient
import datetime
import pprint

client = MongoClient('localhost', 27017)
db = client.test_database

post = {"name":"closer",
        "designer": "raf simons",
        "size": "l",
        "date": datetime.datetime.utcnow()}


print(db.list_collection_names())
pprint.pprint(db.listings.find_one({'size': 'l'}))