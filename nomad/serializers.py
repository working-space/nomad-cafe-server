from django.contrib.auth.models import User as Admin
from .models import Cafe, Member, Rating, Tag
from rest_framework import serializers
from nomad.utils import JSONObjectWriteAndReadField, getListOfTags
from collections import Counter


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
    tags = JSONObjectWriteAndReadField()



class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'url',]


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
            'dist',
            'points'
        ]

    dist = JSONObjectWriteAndReadField()
    location = JSONObjectWriteAndReadField()
    
    tags = serializers.SerializerMethodField()
    def get_tags(self, obj):
        query_result = Rating.objects.mongo_aggregate(getListOfTags(obj.id))
        tags_cnt = {}
        
        for query_object in query_result:
            tag_groups = query_object['tags']
            for tag in tag_groups:
                if tags_cnt.get(tag):
                    tags_cnt[tag] += 1
                else:
                    tags_cnt[tag] = 1

        return tags_cnt


    points = serializers.SerializerMethodField()
    def get_points(self, obj):
        query_result = Rating.objects.mongo_aggregate(getListOfTags(obj.id))
        points_total = 0
        points_cnt = 0

        for query_object in query_result:
            points_total += float(query_object['points'])
            points_cnt += 1

        return points_total / points_cnt if points_cnt > 0 else 0.0