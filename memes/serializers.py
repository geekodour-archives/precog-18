from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
from rest_framework_mongoengine.fields import ObjectIdField

class MemeSerializer(serializers.Serializer):
    id = ObjectIdField(source='_id')
    title = serializers.CharField(required=False, allow_blank=True, max_length=200)
    url = serializers.URLField()
    tags = serializers.ListField(child=serializers.CharField(max_length=100))