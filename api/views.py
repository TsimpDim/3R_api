from rest_framework import routers, serializers, viewsets
from api.models.Resource import Resource
from api.serializers import ResourceSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

''' Permissions:

    Only admin users can get a list of all users
    Only admin can delete users
    Everyone can create a user (register)
    Logged in user can only retrieve/update his own profile.
'''

class ResourceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

    # Limit GET queries to respond only with
    # visible (not-deleted) resources of the current user
    def get_queryset(self):
        queryset = self.queryset
        # If superuser return every resource
        # visible or not
        if self.request.user.is_superuser:
            return queryset
        else:
            query_set = queryset.filter(user=self.request.user).filter(visible=True)
            return query_set