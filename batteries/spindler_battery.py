from batteries.battery import Battery
from utils import add_yrs_to_date

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self): 
        date_that_battery_needs_service_by = add_yrs_to_date(self.last_service_date, 2)
        if date_that_battery_needs_service_by < self.current_date:
            return True
        else: 
            return False
        
            