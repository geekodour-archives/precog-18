from django.db import models
from .customdb import db

def saveToMongo(memeInfo):
    db.meme.insert_one(memeInfo)

class MemeManager(models.Manager):

    def create_meme(self,memeInfo):
        meme = self.model(url = memeInfo['url'])
        saveToMongo(memeInfo)
        meme.save()
        return meme
    
    def return_all(self):
        # create interator object for queryset and mongo thingy
        pass

    def search_meme(self,parsedUserQuery):
        # the raw string query should be LDAd or word2vecd in the view layer and the 
        # proccessed object is parsedUserQuery
        # use custom logic here, call mongo functions to return relevant items
        pass