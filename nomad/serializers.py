from django.contrib.auth.models import User
from .models import Cafe
from rest_framework import serializers


'''
class UserSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='url')
    

    class Meta:
        model = User
        fields = ['url']
'''


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class CafeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cafe
        fields = [
            '_id',
            'create_dt',
            'update_dt',
            'data_id',
            'start_hours',
            'end_hours',
            'location',
            'name',
            'parcel_addr',
            'phone',
            'road_addr',
        ]