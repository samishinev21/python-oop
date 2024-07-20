from unittest import TestCase, main
from car_manager import Car

class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Bugatti", "Mistral", 15, 75)

    def test_init(self):
        self.assertEqual("Bugatti", self.car.make)
        self.assertEqual("Mistral", self.car.model)
        self.assertEqual(15, self.car.fuel_consumption)
        self.assertEqual(75, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_with_empty_string_raise_ex(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_with_empty_string_raise_ex(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_0_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_0_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_negative_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_positive(self):
        self.car.refuel(25)

        self.assertEqual(25, self.car.fuel_amount)

    def test_fuel_negative_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)
        
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_more_than_75(self):
        self.car.refuel(100)

        self.assertEqual(75, self.car.fuel_amount)

    def test_when_needed_is_more_than_fuel_amount_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

if __name__ == "__main__":
    main()