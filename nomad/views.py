from django.contrib.auth.models import User
from .models import Cafe, Location
from rest_framework import viewsets
from rest_framework.response import Response
from nomad.serializers import UserSerializer, CafeSerializer
from nomad.utils import getListByDistance
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
        lat = self.request.query_params.get('lat', None)
        lon = self.request.query_params.get('lon', None)
        _id = self.request.query_params.get('id', None)
        print(lat, lon)
        if _id is not None:
            queryset = queryset.filter(_id=_id)
        if address is not None:
            pass
        if all(pos is not None for pos in [lat, lon]):
            query_result = Cafe.objects.mongo_aggregate(getListByDistance(lat, lon))
            cafe_object = []

            for query_object in query_result:
                location_data = query_object.pop('location')
                dist_data = query_object.pop('dist')
                result = Cafe(**query_object)
                # result.location.add(Location(**location_data), bulk=False)
                cafe_object.append(result)
            
            queryset = cafe_object

        return queryset