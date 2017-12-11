# Connecting to a mongoDB database
# All meme resources and data will be stored in mongoDB

from pymongo import MongoClient

client = MongoClient() # connect to default host and port
db = client['memes'] # will create database 'memes' if does not exist