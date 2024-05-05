from abc import ABC
from car import Car

class Model(ABC):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = self.last_service_mileage
        
    

    @staticmethod
    def create(self):
        pass
       
         
     
    