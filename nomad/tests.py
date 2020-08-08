from django.test import TestCase
from .models import Cafe


class CafeTestCase(TestCase):
    def test_generate(self):
        cafe = Cafe(
                _id = "seoul-data-1009",
                create_dt = "2020-08-02T12:05:22.193+00:00",
                update_dt = "2020-08-02T12:05:22.193+00:00",
                data_id = 1009,
                start_hours = None,
                end_hours = None,
                location = {
                    'type': "Point",
                    'coordinates': [111.1, 122.2],
                },
                name = "TEST",
                parcel_addr = "서울특별시 영등포구 문래동2가 21-2번지 ",
                phone = "010-0000-0000",
                road_addr = "서울특별시 영등포구 문래동2가 21-2번지 "
            )
        print(cafe._id)
        self.assertTrue(cafe._id == "seoul-data-1009")
