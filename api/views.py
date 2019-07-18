from rest_framework import routers, serializers, viewsets
from api.models.Resource import Resource
from api.serializers import ResourceSerializer

''' Permissions:

    Only admin users can get a list of all users
    Only admin can delete users
    Everyone can create a user (register)
    Logged in user can only retrieve/update his own profile.
'''

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
