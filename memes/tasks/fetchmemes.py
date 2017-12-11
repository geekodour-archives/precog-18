from django.conf import settings

# third party imports
import requests
import time
import io
from urllib.request import urlopen

# 3rd party
import pytesseract
from PIL import Image
from bs4 import BeautifulSoup

# custom imports
from memes.models import Meme


class BaseMemeFetcher:
    """Base Class for Fetcher"""

    initialMemeFetchCount = 500
    regularMemeFetchCount = 20

    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    }

    memeInfo = {
        'url':'',
        'title':'',
        'tags': [],
        'source': None,
        'description': '',
        'extracted_text': ''
    }

    @staticmethod
    def extractTextFromImage(memeInfo):
        r = requests.get(memeInfo['url'])
        img = Image.open(io.BytesIO(r.content))
        memeInfo['extracted_text'] = pytesseract.image_to_string(img)
        print(memeInfo)

    def eachSourceCount(self,totalFetchCount):
        '''Returns the count of memes to be fetched from sub-sources'''
        return totalFetchCount//len(self.baseApiUrls)

    @classmethod
    def saveMemes(cls,memeList):
        [cls.extractTextFromImage(p) for p in memeList]
        print(memeList)
        # save the memeList now

    @classmethod
    def addDelay(cls,func):
        ''' Delay is not needed, adding for safety '''
        def wrapper(self,*args,**kwargs):
            time.sleep(1)
            func(self,*args,**kwargs)
        return wrapper

class RedditMemeFetcher(BaseMemeFetcher):
    source = 'reddit'
    memes_fetched_foreach = 0
    baseApiUrls = [
        'https://www.reddit.com/r/memes/',
        'https://www.reddit.com/r/wholesomememes/',
    ]

    def generateUrl(self,subreddit,sort='',time='',limit=100,lastPostName=''):
        return '{}{}/.json?t={}&limit={}&after={}'.format(subreddit,sort,time,limit,lastPostName)
    
    def getInitialMemes(self):
        count = self.initialMemeFetchCount
        eachCount = self.eachSourceCount(count)
        for index,apiurl in enumerate(self.baseApiUrls):
            self.memes_fetched_foreach = 0
            url = self.generateUrl(apiurl,'top','year',100)
            self.fetchMemes(url,eachCount,index)

    def getRegularMemes(self):
        count = self.regularMemeFetchCount
        eachCount = self.eachSourceCount(count)

    def extractMemeInfo(self,post):
        tmp = self.memeInfo.copy()
        tmp['url'] = post['data']['url']
        tmp['title'] = post['data']['title']
        tmp['source'] = self.source
        return tmp

    @BaseMemeFetcher.addDelay
    def fetchMemes(self,url,count,index):
        r = requests.get(url,headers=self.headers)
        data = r.json()['data']
        lastPostName = data['after']
        self.memes_fetched_foreach += len(data['children'])
        if(self.memes_fetched_foreach>=count):
            posts = [d for d in data['children'] if not d['data']['is_self']][0:count]
            posts = [self.extractMemeInfo(post) for post in posts]
            self.saveMemes(posts)
        else:
            posts = [d for d in data['children'] if not d['data']['is_self']]
            posts = [self.extractMemeInfo(post) for post in posts]
            self.saveMemes(posts)
            url = self.generateUrl(self.baseApiUrls[index],'top','year',50,lastPostName)
            self.fetchMemes(url,count,index)


class GiphyMemeFetcher(BaseMemeFetcher):
    source = 'giphy'
    API_KEY = settings.GIPHY_API_KEY
    memes_fetched_foreach = 0
    baseApiUrls = [
        'https://api.giphy.com/v1/gifs/trending'
    ]

    def generateUrl(self,url,limit=100):
        return '{}?api_key={}&limit={}'.format(url,self.API_KEY,limit)

    def extractMemeInfo(self,post):
        tmp = self.memeInfo.copy()
        tmp['url'] = post['images']['original_still']
        # "https://media1.giphy.com/media/uk746NM22sIbC/200_s.gif",
        tmp['title'] = post['title']
        tmp['source'] = self.source
        tmp['tags'] = self.fetchTags(post['url'])
        return tmp

    def fetchTags(self,postUrl):
        raw_data = urlopen(postUrl)
        html = raw_data.read().decode('utf-8')
        soup = BeautifulSoup(html,'html.parser')
        return soup.find(attrs={'name':'keywords'})['content'].split(',')[:-2]

    @BaseMemeFetcher.addDelay
    def fetchMemes(self,url,count):
        r = requests.get(url,headers=self.headers)
        data = r.json()
        posts = [self.extractMemeInfo(post) for post in data['data']]
        self.saveMemes(posts)

    def getInitialMemes(self):
        count = self.initialMemeFetchCount
        url = self.generateUrl(self.baseApiUrls[0],10) # PUT INITIAL HERE
        self.fetchMemes(url,10)
    
    def getRegularMemes():
        count = self.regularMemeFetchCount
        url = generateUrl(self.baseApiUrls[0],10) # PUT REGULAR HERE HERE

    def getTheOfficeMemes():
        count = 100 # HARDDDDD