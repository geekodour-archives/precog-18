# Connecting to a mongoDB database
# All meme resources and data will be stored in mongoDB

from django.conf import settings
from pymongo import MongoClient

if(settings.DEBUG):
    client = MongoClient() # connect to default host and port
else:
    client = MongoClient('mongodb://geekodour:precog2018@ds139446.mlab.com:39446/memehunter') #mlab
db = client['memes'] # will create database 'memes' if does not exist