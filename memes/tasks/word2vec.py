"""
The memes are topic modelled here, based on their
1. extractd text
2. topic
3. tags
"""
from django.conf import settings
import numpy as np
import gensim
from memes.customdb import db

model = gensim.models.KeyedVectors.load_word2vec_format(str(settings.W2V_PATH), binary=True)

def avg_sentence(sentence):
    v = np.zeros(300)
    for w in sentence:
        if w in model.wv:
            v += model.wv[w]
    return v / len(sentence)

def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def getClosestTags(wordorphase):
    avgWord = avg_sentence(wordorphase.split())
    tags = db.meme.distinct('tags')
    avgTags = [(i,avg_sentence(i)) for i in tags]
    similarity = [(i,cosine_sim(avgWord,j)) for i,j in avgTags]
    most_similar_meme = sorted(similarity, key=lambda p: p[1], reverse=True)
    return most_similar_meme