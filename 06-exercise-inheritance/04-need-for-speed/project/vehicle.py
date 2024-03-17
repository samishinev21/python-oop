class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = 1.25
        Vehicle.DEFAULT_FUEL_CONSUMPTION = self.fuel_consumption

    def drive(self, kilometers):
        needed_fuel = kilometers * self.fuel_consumption

        if self.fuel >= needed_fuel:
            self.fuel -= needed_fuel