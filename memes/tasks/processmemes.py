"""
The memes are topic modelled here, based on their
1. extractd text
2. topic
3. tags
"""
from django.conf import settings
import gensim

#model = gensim.models.KeyedVectors.load_word2vec_format(str(settings.W2V_PATH), binary=True)