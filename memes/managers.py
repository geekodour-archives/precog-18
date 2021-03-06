from django.db import models
from .customdb import db
from bson.objectid import ObjectId

from memes.tasks.word2vec import getClosestTags 

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
        ''' Efficient but fails on duplicates '''
        memeObjList = [self.model(url = m['url'],mongoid = str(m['_id'])) for m in memeList]
        self.model.objects.bulk_create(memeObjList)
        db.meme.insert_many(memeList)

    def create_from_meme_list_single(self,memeList):
        ''' This is not efficient but ignores duplicate entries '''
        for m in memeList:
            self.create_meme(m)
    
    def return_all(self,limit=1000):
        return db.meme.find().limit(limit)

    def get(self,id):
        return db.meme.find_one({'_id':ObjectId(id)})

    def text_search_meme(self,parsedUserQuery,limit=50):
        #return db.meme.find({'$text':{'$search': parsedUserQuery}}, { score : { $meta: “textScore” } }).sort({ score: { $meta : ‘textScore’ } }).limit(limit)
        return db.meme.find(
            { '$text': { '$search': parsedUserQuery } },
        ).limit(limit)

    def tag_search_meme(self,wordList,limit=50):
        return db.meme.find({'tags': {'$in': wordList} }).limit(limit)

    def tag_search_meme_w2v(self,wordList,limit=50):
        tagList = []
        for i in wordList:
            sim = [j for j in getClosestTags(i) if j[1]>0.001]
            for j in sim:
                tagList.append(j[0])

        return db.meme.find({'tags': {'$in': tagList} }).limit(limit)