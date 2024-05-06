from tires.tire import Tire
from utils import add_yrs_to_date

class Octoprime(Tire):
    def __init__(self, wear=[]):
        self.wear = wear

    def needs_service(self):
        return sum(self.wear) >= 3
            