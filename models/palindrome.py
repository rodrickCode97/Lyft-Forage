from datetime import datetime
from abc import ABC
from car import Car


from models.model import Model 
from engine.sternman_engine import SternmanEngine
from batteries.spindler_battery import SpindlerBattery

# class Palindrome(SternmanEngine):
#     def needs_service(self):
#         service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
#         if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
#             return True
#         else:
#             return False
        

class Palindrome(Model):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(current_date, last_service_date, current_mileage, last_service_mileage)
    def create(self):
        engine = SternmanEngine(self.current_mileage, self.last_service_date)
        battery = SpindlerBattery(self.current_date, self.last_service_date)
        car = Car(engine, battery)
        return car
