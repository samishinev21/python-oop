from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 300)

    def test_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(300, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_fuel_lower_than_fuel_needed_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100000000000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_you_have_enough_fuel_fuel_minus_fuel_needed(self):
        self.vehicle.drive(0)

        self.assertEqual(100, self.vehicle.fuel)

    def test_fuel_to_much_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10000000000000000)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_not_to_much_fuel_add_fuel(self):
        self.vehicle.refuel(0)

        self.assertEqual(100, self.vehicle.fuel)

    def test_string(self):
        self.assertEqual(
            "The vehicle has 300 horse power with 100 fuel left and 1.25 fuel consumption",
            self.vehicle.__str__()
        )


if __name__ == "__main__":
    main()
