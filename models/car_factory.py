from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from car import Car



class CarFactory:
    @staticmethod
    def calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery= SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
    @staticmethod
    def glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
    @staticmethod
    def palindrome(current_date, last_service_date, warning_light_is_on):
            engine = SternmanEngine(warning_light_is_on)
            battery = SpindlerBattery(current_date, last_service_date)
            car = Car(engine, battery)
            return car
    @staticmethod
    def thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_date)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
    @staticmethod
    def rorscharch(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_date)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car