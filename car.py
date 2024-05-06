from service import Service
from abc import ABC


# class Car(ABC):
#     def __init__(self, last_service_date):
#         self.last_service_date = last_service_date

#     @abstractmethod
#     def needs_service(self):
#         pass


class Car(ABC): 
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires
    
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()

