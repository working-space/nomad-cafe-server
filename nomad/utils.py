from rest_framework import serializers
import json

class JSONObjectWriteAndReadField(serializers.Field):

    def to_representation(self, obj):
        return obj

    def to_internal_value(self, data):
        if isinstance(data, str):
            data = json.loads(data.replace("'", '"'))
            
        return data


def getListByDistance(lat, lon):
    query = [
                {
                    "$geoNear": {
                        "near": {
                            "type": "Point",
                            "coordinates": [float(lat), float(lon)]
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