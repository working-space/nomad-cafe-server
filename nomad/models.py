from django.db import models
from djongo import models as mongo_models

class Tag(mongo_models.Model):
    id = mongo_models.CharField(db_column='_id', max_length=512, primary_key=True)
    name = mongo_models.CharField(max_length=512)


    class Meta:
        # app_label = 'default'
        db_table = 'tag'


class Member(mongo_models.Model):
    id = mongo_models.CharField(db_column='_id', max_length=512, primary_key=True)
    # name : this key is made by IP and specified key(ex: browser cookie key...)
    name = mongo_models.CharField(max_length=512)
    create_dt = mongo_models.DateTimeField(auto_now_add=True)
    update_dt = mongo_models.DateTimeField(auto_now=True)


    class Meta:
        # app_label = 'default'
        db_table = 'user'


class Rating(mongo_models.Model):
    id = mongo_models.CharField(db_column='_id', max_length=512, primary_key=True)
    cafe_id = mongo_models.CharField(max_length=512)
    user_id = mongo_models.CharField(max_length=512)
    tags = mongo_models.JSONField()
    points = mongo_models.DecimalField(max_digits=5, decimal_places=3)
    create_dt = mongo_models.DateTimeField(auto_now_add=True)
    update_dt = mongo_models.DateTimeField(auto_now=True)

    objects = mongo_models.DjongoManager()


    class Meta:
        # app_label = 'default'
        db_table = 'rating'


class Location(mongo_models.Model):
    type = mongo_models.CharField(max_length=128)
    coordinates = mongo_models.CharField(max_length=512)


    class Meta:
        abstract = True


class Cafe(mongo_models.Model):
    id = mongo_models.CharField(db_column='_id', max_length=512, primary_key=True)
    data_id = mongo_models.CharField(max_length=512)
    data_type = mongo_models.CharField(max_length=512)
    create_dt = mongo_models.DateTimeField(auto_now_add=True)
    update_dt = mongo_models.DateTimeField(auto_now=True)
    data_id = mongo_models.IntegerField()
    start_hours = mongo_models.CharField(max_length=512)
    end_hours = mongo_models.CharField(max_length=512)
    location = mongo_models.JSONField()
    name = mongo_models.CharField(max_length=512)
    brand_name = mongo_models.CharField(max_length=512)
    x = mongo_models.CharField(max_length=64)
    y = mongo_models.CharField(max_length=64)
    parcel_addr = mongo_models.CharField(max_length=512)
    zipcode = mongo_models.CharField(max_length=512)
    phone = mongo_models.CharField(max_length=32)
    road_addr = mongo_models.CharField(max_length=512)
    homepage = mongo_models.CharField(max_length=512)
    img = mongo_models.CharField(max_length=512)
    tags = mongo_models.JSONField()
    region_1depth_name = mongo_models.CharField(max_length=512)
    region_2depth_name = mongo_models.CharField(max_length=512)
    region_3depth_name = mongo_models.CharField(max_length=512)
    road_name = mongo_models.CharField(max_length=512)
    dist = mongo_models.JSONField()

    objects = mongo_models.DjongoManager()


    class Meta:
        # app_label = 'default'
        db_table = 'cafe'
