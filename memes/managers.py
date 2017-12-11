from django.db import models

class MemeManager(models.Manager):

    def create_meme(self,memeInfo):
        meme = self.model(url = memeInfo['url'])
        meme.save()
        return meme