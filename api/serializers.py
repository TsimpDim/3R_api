from rest_framework import serializers
from api.models.Resource import Resource
from django.contrib.auth.models import User

'''
 Converts to JSON and validates data
'''
class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__' # ['id', 'title', 'url', 'note', 'tags', 'date_of_creation']
