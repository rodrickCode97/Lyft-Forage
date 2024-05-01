from datetime import datetime
from abc import ABC
from car import Car 

from engine.willoughby_engine import WilloughbyEngine


# class Glissade(WilloughbyEngine):
#     def needs_service(self):
#         service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
#         if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
#             return True
#         else:
#             return False


class Glissade(Car):
    def __init__(self, last_service_date, parts):
           super().__init__(last_service_date, parts)
           self.last_service_date = datetime.today()
           self.parts = [WilloughbyEngine]
    def needs_service(self):
        for part in self.parts:
             if part.needs_service() is True:
                  return True 
        return False