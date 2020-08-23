from rest_framework import serializers
import json

class JSONObjectWriteAndReadField(serializers.Field):

    def to_representation(self, obj):
        return obj

    def to_internal_value(self, data):
        if isinstance(data, str):
            data = json.loads(data.replace("'", '"'))

        return data


def getCountOfTags(id):
    query = [
                {"$match":{"cafe_id":id}},
                {"$unwind":"$tags"},
                {"$group":{"_id":"$tags","count":{"$sum":1}}},
                {"$group":{"_id":None,"tags":{"$push":{"id":"$_id",
                                                            "count":"$count"}}}},
                
                {"$project":{"_id":0,"tags":1}}
            ]
    return query


# TODO: Float 변환 부분 수정
def getAvgOfPoints(id):
    query = [
                {"$match":{"cafe_id":id}},
                # {"$group":{"_id":None,"pop":{"$avg":{'input': "$points", 'to': 'float'}}}}
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