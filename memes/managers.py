from django.db import models
from .customdb import db

class MemeManager(models.Manager):

    def create_meme(self,memeInfo):
        try:
            meme = self.model(url = memeInfo['url'], mongoid = str(memeInfo['_id']))
            meme.save()
            db.meme.insert_one(memeInfo)
            return meme
        except Exception:
            pass

    def create_from_meme_list(self,memeList):
        memeObjList = [self.model(url = m['url'],mongoid = str(m['_id'])) for m in memeList]
        self.model.objects.bulk_create(memeObjList)
        db.meme.insert_many(memeList)

    def create_from_meme_list_single(self,memeList):
        ''' This is not efficient but ignores duplicate entries '''
        for m in memeList:
            self.create_meme(m)
    
    def return_all(self):
        # create interator object for queryset and mongo thingy
        pass

    def search_meme(self,parsedUserQuery):
        # the raw string query should be LDAd or word2vecd in the view layer and the 
        # proccessed object is parsedUserQuery
        # use custom logic here, call mongo functions to return relevant items
        pass