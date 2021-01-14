from django.contrib.auth.models import User as Admin
from django.db import transaction
from django.db.models import F
from .models import Cafe, Location, Member, Rating, Tag
from rest_framework import viewsets
from rest_framework.response import Response
from nomad.serializers import MemberSerializer, CafeSerializer, RatingSerializer, AdminSerializer, TagSerializer
from nomad.utils import getListByDistance, getCountOfTags, getAvgOfPoints

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all().order_by('-date_joined')
    serializer_class = AdminSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    
    @transaction.atomic
    def _update_tags_and_avg_points(self, request, *args, **kwargs): 
        cafe_id = request.data['cafe_id']
        cafe_obj = Cafe.objects.get(pk=cafe_id)

        # Get tags
        query_result = list(Rating.objects.mongo_aggregate(getCountOfTags(cafe_id)))
        tags = []

        if query_result:
            for tag in query_result[0]['tags']:
                tag = dict(tag)
                tag['name'] = Tag.objects.get(id=tag['id']).name
                tags.append(tag)

        # Commit tags
        cafe_obj.tags = tags

        # Get points
        query_result = list(Rating.objects.mongo_aggregate(getAvgOfPoints(cafe_id)))
        points_total = 0
        points_cnt = 0

        for query_object in query_result:
            points_total += float(query_object['points'])
            points_cnt += 1

        # Commit points
        cafe_obj.points = points_total / points_cnt if points_cnt > 0 else 0.0

        # Save tags and points
        cafe_obj.save(update_fields=['tags', 'points'])
        
        return None

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super().retrieve(request, pk, *args, **kwargs)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        result = super().create(request, *args, **kwargs)
        self._update_tags_and_avg_points(request, *args, **kwargs)

        return result
    
    @transaction.atomic
    def update(self, request, pk=None, *args, **kwargs):
        result = super().update(request, pk, *args, **kwargs)
        self._update_tags_and_avg_points(request, *args, **kwargs)

        return result

    @transaction.atomic
    def partial_update(self, request, pk=None, *args, **kwargs):
        result = super().partial_update(request, pk, *args, **kwargs)
        self._update_tags_and_avg_points(request, *args, **kwargs)

        return result


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CafeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cafe.objects.all() 
    serializer_class = CafeSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        lon = request.query_params.get('lon', None)
        lat = request.query_params.get('lat', None)

        if lon is None or lat is None:
            return super().retrieve(request, *args, **kwargs)

        instance = self._getDistanceByPosition(lon=lon, lat=lat, pk=pk)

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
        dist = self.request.query_params.get('dist', None)

        if address is not None:
            pass

        queryset = self._getDistanceByPosition(lon=lon, lat=lat, dist=dist)

        return queryset

    def _getDistanceByPosition(self, lon, lat, dist=None, pk=None):
        queryset = self.queryset
        
        if all(pos is not None for pos in [lon, lat]):
            query_result = Cafe.objects.mongo_aggregate(getListByDistance(lon, lat, dist, pk))
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