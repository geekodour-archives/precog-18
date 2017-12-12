from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Meme
#from .serializers import CustomMemeSerializer
from .serializers import MemeSerializer

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

