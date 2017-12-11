from memes.models import Meme

class BaseMemeFetcher:
    """Base Class for Fetcher"""

    initialMemeFetchCount = 500
    regularMemeFetchCount = 20

    memeInfo = {
        'url':'',
        'title':'',
        'tags': [],
        'source': None,
        'description': '',
        'extracted_text': ''
    }

    @classmethod
    def saveMeme(self):
        pass

class RedditMemeFetcher(BaseMemeFetcher):
    source = "reddit"
    baseApiUrls = []
    def getInitialMemes(self):
        count = self.initialMemeFetchCount
    
    def getRegularMemes():
        count = self.regularMemeFetchCount
        pass

class GiphyMemeFetcher(BaseMemeFetcher):
    source = "giphy"
    baseApiUrls = []
    def getInitialMemes(self):
        baseApiUrls = self.sources['reddit']['api']
    
    def getRegularMemes():
        pass

    def getTheOfficeMemes():
        count = 100 # HARDDDDD