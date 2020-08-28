from django.contrib.auth.models import User as Admin
from django.db.models import F
from .models import Cafe, Location, Member, Rating, Tag
from rest_framework import viewsets
from rest_framework.response import Response
from nomad.serializers import MemberSerializer, CafeSerializer, RatingSerializer, AdminSerializer, TagSerializer
from nomad.utils import getListByDistance


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all().order_by('-date_joined')
    serializer_class = AdminSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CafeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cafe.objects.all() 
    serializer_class = CafeSerializer

    def retrieve(self, request, pk=None):
        lon = request.query_params.get('lon', None)
        lat = request.query_params.get('lat', None)

        instance = self._getDistanceByPosition(lon, lat, pk)

        if instance:
            serializer = self.get_serializer(instance[0])

            return Response(serializer.data)
        else:
             return Response({"detail": "Not found."})

    def get_queryset(self):
        queryset = self.queryset

        address = self.request.query_params.get('address', None)
        lon = self.request.query_params.get('lon', None)
        lat = self.request.query_params.get('lat', None)

        if address is not None:
            pass

        queryset = self._getDistanceByPosition(lon, lat)

        return queryset

    def _getDistanceByPosition(self, lon, lat, pk=None):
        queryset = self.queryset
        
        if all(pos is not None for pos in [lon, lat]):
            query_result = Cafe.objects.mongo_aggregate(getListByDistance(lon, lat, pk))
            cafe_object = []

            for query_object in query_result:
                dist = query_object.pop('dist')
                id = query_object.pop('_id')
                
                result = Cafe(**query_object)
                
                result.dist = dist
                result.id = id
                
                cafe_object.append(result)


            queryset = cafe_object

        return queryset