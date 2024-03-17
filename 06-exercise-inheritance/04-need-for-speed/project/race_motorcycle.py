from project.motorcycle import Motorcycle

class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = 8
        RaceMotorcycle.DEFAULT_FUEL_CONSUMPTION = self.fuel_consumption