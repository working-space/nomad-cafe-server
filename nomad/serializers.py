from django.contrib.auth.models import User as Admin
from .models import Cafe, Member, Rating, Tag
from rest_framework import serializers


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = [
            'id',
            'cafe_id',
            'user_id',
            'tags',
            'points',
            'create_dt',
            'update_dt',
            'url', 
        ]


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'url', ]


class AdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Admin
        fields = ['url', 'username', 'email', 'groups']


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = [
            'id',
            'name',
            'create_dt',
            'update_dt',
            'url', 
        ]


class CafeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cafe
        fields = [
            'id',
            'data_id',
            'data_type',
            'create_dt',
            'update_dt',
            'data_id',
            'start_hours',
            'end_hours',
            'location',
            'name',
            'brand_name',
            'x',
            'y',
            'parcel_addr',
            'zipcode',
            'phone',
            'road_addr',
            'homepage',
            'img',
            'tags',
            'region_1depth_name',
            'region_2depth_name',
            'region_3depth_name',
            'road_name',
            'url', 
        ]