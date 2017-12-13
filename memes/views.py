from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Meme
from .serializers import MemeSerializer
from .tasks.tokenize import tokenize

class MemeList(APIView):

    def get(self, request, format=None):
        l = list(Meme.objects.return_all(limit=100))
        l = MemeSerializer(l, many=True)
        return Response(l.data)


class MemeDetail(APIView):

    def get(self, request, pk, format=None):
        try:
            l = Meme.objects.get(pk)
            l = MemeSerializer(l)
            return Response(l.data)
        except Exception:
            raise Http404

class MemeSearch(APIView):

    def get(self, request, format=None):
        query = self.request.query_params.get('q',None)
        queryTokens = query.split(',')
        queryTokens2 = tokenize(query)
        l1 = list(Meme.objects.text_search_meme(query))
        l2 = list(Meme.objects.tag_search_meme(queryTokens))
        l3 = list(Meme.objects.tag_search_meme_w2v(queryTokens2))
        l = MemeSerializer(l1+l2+l3, many=True)
        return Response(l.data)