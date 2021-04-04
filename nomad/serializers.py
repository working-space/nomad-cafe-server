from django.contrib.auth.models import User as Admin
from .models import Cafe, Member, Rating, Tag, Comment, Bookmark
from rest_framework import serializers
from nomad.utils import JSONObjectWriteAndReadField, getCountOfTags, getAvgOfPoints
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
        example = {
            "id": "ratings-id-1",
            "cafe_id": "cafe-id-1",
            "user_id": "user-id-1",
            "tags": [
                "tag-id-1",
                "tag-id-2",
                "tag-id-3"
            ],
            "points": 3.4
        }
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
            'nickname',
            'profile_image',
            'oauth_vender',
            'refresh_token',
            'access_token',
            'oauth_id',
            'favorite_cafes',
            'create_dt',
            'update_dt',
            'url',
        ]

    favorite_cafes = JSONObjectWriteAndReadField()


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookmark
        fields = [
            'id',
            'cafe_id',
            'user_id',
            'create_dt',
            'update_dt',
        ]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'cafe_id',
            'user_id',
            'content',
            'create_dt',
            'update_dt',
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
            'comments',
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

    tags = JSONObjectWriteAndReadField()
    comments = JSONObjectWriteAndReadField()