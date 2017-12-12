from rest_framework import serializers

class MemeSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=200)
    url = serializers.URLField()
    tags = serializers.ListField(child=serializers.CharField(max_length=100))

'''
class CustomMemeSerializer(memeObject):
    if(type(memeObject) == list):
        for m in memeObject:
            m['_id'] = str(m['_id']) 
    else:
        memeObject['_id'] = str(memeObject['_id'])
'''