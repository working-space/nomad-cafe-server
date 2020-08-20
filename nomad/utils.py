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