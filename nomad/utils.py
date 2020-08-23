from rest_framework import serializers
import json

class JSONObjectWriteAndReadField(serializers.Field):

    def to_representation(self, obj):
        return obj

    def to_internal_value(self, data):
        if isinstance(data, str):
            data = json.loads(data.replace("'", '"'))

        return data


def getListOfTags(id):
    query = [
                {
                    "$match": {
                        "cafe_id": id
                    }
                }
            ]
    return query


def getListByDistance(lon, lat):
    query = [
                {
                    "$geoNear": {
                        "near": {
                            "type": "Point",
                            "coordinates": [float(lon), float(lat)]
                        },
                        # "spherical": "true",
                        "key": "location",
                        "maxDistance": 5000,
                        "distanceField": "dist.calculated",
                        "query": {
                            "road_addr": {"$regex": '^서울'}
                        }
                    }
                },
                {"$limit": 5000}
            ]
    return query