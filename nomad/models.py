from django.db import models
from djongo import models as mongo_models
from django.contrib.postgres.fields import JSONField


class Location(mongo_models.Model):
    type = mongo_models.CharField(max_length=128)
    coordinates = JSONField()


    class Meta:
        abstract = True


class Cafe(mongo_models.Model):
    _id = mongo_models.CharField(max_length=512)
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
    parcel_addr = mongo_models.CharField(max_length=512)
    phone = mongo_models.CharField(max_length=32)
    road_addr = mongo_models.CharField(max_length=512)
    tags = mongo_models.CharField(max_length=512)

    objects = mongo_models.DjongoManager()

    class Meta:
        app_label = 'MongoDB'
        db_table = 'cafe'