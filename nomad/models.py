from django.db import models
from djongo import models as mongo_models
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import ArrayField

class Tag(mongo_models.Model):
    id = mongo_models.CharField(db_column='_id', max_length=512, primary_key=True)
    name = mongo_models.CharField(max_length=512)


    class Meta:
        app_label = 'MongoDB'
        db_table = 'tag'


class User(mongo_models.Model):
    id = mongo_models.CharField(db_column='_id', max_length=512, primary_key=True)
    # name : this key is made by IP and specified key(ex: browser cookie key...)
    name = mongo_models.CharField(max_length=512)
    create_dt = mongo_models.DateTimeField()
    update_dt = mongo_models.DateTimeField()


    class Meta:
        app_label = 'MongoDB'
        db_table = 'user'


class Rating(mongo_models.Model):
    id = mongo_models.CharField(db_column='_id', max_length=512, primary_key=True)
    cafe_id = mongo_models.CharField(max_length=512)
    user_id = mongo_models.CharField(max_length=512)
    tags = ArrayField(mongo_models.CharField(max_length=512))
    create_dt = mongo_models.DateTimeField()
    update_dt = mongo_models.DateTimeField()


    class Meta:
        app_label = 'MongoDB'
        db_table = 'rating'


class Location(mongo_models.Model):
    type = mongo_models.CharField(max_length=128)
    coordinates = ArrayField(mongo_models.DecimalField())


    class Meta:
        abstract = True


class Cafe(mongo_models.Model):
    id = mongo_models.CharField(db_column='_id', max_length=512, primary_key=True)
    data_id = mongo_models.CharField(max_length=512)
    data_type = mongo_models.CharField(max_length=512)
    create_dt = mongo_models.DateTimeField()
    update_dt = mongo_models.DateTimeField()
    data_id = mongo_models.IntegerField()
    start_hours = mongo_models.CharField(max_length=512)
    end_hours = mongo_models.CharField(max_length=512)
    location = mongo_models.EmbeddedField(
        model_container=Location,
        null=True,
        blank=True
    )
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
    tags = ArrayField(JSONField())

    objects = mongo_models.DjongoManager()


    class Meta:
        app_label = 'MongoDB'
        db_table = 'cafe'
