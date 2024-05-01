from datetime import datetime
from abc import ABC
from car import Car 

from engine.capulet_engine import CapuletEngine


# class Thovex(CapuletEngine):
#     def needs_service(self):
#         service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
#         if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
#             return True
#         else:
#             return False

class Thovex(Car):
    def __init__(self, last_service_date, parts):
        super().__init__(last_service_date, parts)
        self.last_service_date = datetime.today()
        self.parts = [CapuletEngine]
    def needs_service(self):
        for part in self.parts:
            if part.needs_service() is True:
                return True
        return False 
       
