from django.db import models
from djongo import models as mongo_models


class Location(models.Model):
    type = mongo_models.CharField(max_length=128)
    # coordinates = mongo_models.ArrayField(
    #     mongo_models.DecimalField(max_digits=19, decimal_places=10)
    # )


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
        model_container=Location
    )
    name = mongo_models.CharField(max_length=512)
    parcel_addr = mongo_models.CharField(max_length=512)
    phone = mongo_models.CharField(max_length=32)
    road_addr = mongo_models.CharField(max_length=512)
    tags = mongo_models.CharField(max_length=512)

    class Meta:
        app_label = 'MongoDB' 
