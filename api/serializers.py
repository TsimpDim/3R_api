from rest_framework import serializers
from api.models.Resource import Resource
from api.models.Option import Option
from django.contrib.auth.models import User

'''
 Converts to JSON and validates data
'''
class ResourceSerializer(serializers.ModelSerializer):
    # We need a way to assign the user_id
    # Especially since we don't store it client-side (we only store the token)
    # This way, we get the current user automatically and make the field Hidden
    # i.e you cannot set it based on user input
    # 
    # <!> This works because we are using a ViewSet and the context
    # is passed to the serializer automatically
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Resource
        fields = '__all__' # ['id', 'title', 'url', 'note', 'tags', 'date_of_creation']


class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = ['sort']