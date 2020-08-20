from django.contrib.auth.models import User as Admin
from django.db.models import F
from .models import Cafe, Location, Member, Rating, Tag
from rest_framework import viewsets
from rest_framework.response import Response
from nomad.serializers import MemberSerializer, CafeSerializer, RatingSerializer, AdminSerializer, TagSerializer
from nomad.utils import getListByDistance
# from django.shortcuts import render


class AdminViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
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

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     # serializer = self.get_serializer(data=request.data,many=isinstance(request.data, list), partial=True)
    #     serializer = self.get_serializer(instance, data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     if request.user.has_perm('change_monitor', instance):
    #         instance = serializer.save()
    #         self.perform_update(instance)
    #         headers = self.get_success_headers(serializer.validated_data)
    #         return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT, headers=headers)
    #     else:
    #         return HttpResponseForbidden('Somehow, you aren\'t authorized to update')


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
        id = self.request.query_params.get('id', None)

        if id is not None:
            queryset = queryset.filter(id=id)
        if address is not None:
            pass
        if all(pos is not None for pos in [lat, lon]):
            query_result = Cafe.objects.mongo_aggregate(getListByDistance(lat, lon))
            cafe_object = []

            for query_object in query_result:
                dist_data = query_object.pop('dist')
                id = query_object.pop('_id')
                
                result = Cafe(**query_object)
                
                result.dist = dist_data
                result.id = id
                
                cafe_object.append(result)

            queryset = cafe_object

        return queryset