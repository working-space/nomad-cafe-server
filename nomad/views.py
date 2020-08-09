from django.contrib.auth.models import User
from .models import Cafe
from rest_framework import viewsets
from rest_framework.response import Response
from nomad.serializers import UserSerializer, CafeSerializer
# from django.shortcuts import render


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CafeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cafe.objects.all() 
    serializer_class = CafeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset
        address = self.request.query_params.get('address', None)
        _id = self.request.query_params.get('id', None)
        if _id is not None:
            queryset = queryset.filter(_id=_id)
        if address is not None:
            queryset = queryset.filter(road_addr=address)
        return queryset