from datetime import datetime
from car import Car 
from abc import ABC 
from models.model import Model

from engine.willoughby_engine import WilloughbyEngine
from batteries.nubbin_battery import NubbinBattery


# class Rorschach(WilloughbyEngine):
#     def needs_service(self):
#         service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
#         if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
#             return True
#         else:
#             return False

class Rorschach(Model):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(current_date, last_service_date, current_mileage, last_service_mileage)
    def create(self):
        engine = WilloughbyEngine(self.current_mileage, self.last_service_date)
        battery = NubbinBattery(self.current_date, self.last_service_date)
        car = Car(engine, battery)
        return car
