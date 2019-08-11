from rest_framework import routers, serializers, viewsets
from api.models.Resource import Resource
from api.models.Option import Option
from rest_framework.response import Response
from api.serializers import ResourceSerializer, OptionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.contrib.auth.models import User
import rest_framework.generics as gen
from django.shortcuts import get_object_or_404

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
    # visible (not-removed) resources of the current user
    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user).filter(visible=True)
        
        options = Option.objects.get(user=self.request.user)

        if options.sort == 'AAS':
            queryset = queryset.order_by('title')
        elif options.sort == 'ADE':
            queryset = queryset.order_by('-title')
        elif options.sort == 'TAS':
            queryset = queryset.order_by('date_of_creation')
        elif options.sort == 'TDE':
            queryset = queryset.order_by('-date_of_creation')

        return queryset


class RemovedResourceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

    # Perhaps these can be condensed in one line above?
    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user).filter(visible=False)
        return query_set

class OptionRetrieveUpdateView(gen.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OptionSerializer

    def get_queryset(self):
        return Option.objects.filter(user_id=self.request.user)

    # This allows us to get a single object instead of a single object in an array
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj