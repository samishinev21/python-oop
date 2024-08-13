from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailWay(TestCase):

    def setUp(self):
        self.station = RailwayStation("Oxford")

    def test_init(self):
        self.assertEqual("Oxford", self.station.name)
        self.assertEqual(deque([]), self.station.arrival_trains)
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_name_when_valid(self):
        self.station.name = "Burgas"

        self.assertEqual("Burgas", self.station.name)

    def test_name_when_invalid(self):
        with self.assertRaises(Exception) as ex:
            self.station.name = "BS"

        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board("Train1")

        self.assertEqual(deque(["Train1"]), self.station.arrival_trains)

    def test_train_has_arrived_empty_arrival_trains(self):
        self.station.arrival_trains = deque()

        with self.assertRaises(IndexError) as error:
            self.station.train_has_arrived("Sofia")

        self.assertEqual("pop from an empty deque", str(error.exception))

    def test_train_has_arrived_when_other_trains_on_the_queue(self):
        self.station.arrival_trains = deque(["Varna"])

        result = self.station.train_has_arrived("Sofia")

        self.assertEqual("There are other trains to arrive before Sofia.", result)

    def test_train_has_arrived_when_no_other_trains(self):
        self.station.arrival_trains = deque(["Varna"])

        result = self.station.train_has_arrived("Varna")

        self.assertEqual(deque(["Varna"]), self.station.departure_trains)

        self.assertEqual("Varna is on the platform and will leave in 5 minutes.", result)

    def test_train_has_left_when_empty_departure_trains(self):
        self.station.departure_trains = deque()

        result = self.station.train_has_left("Sofia")

        self.assertEqual(False, result)

    def test_train_has_left_when_other_trains_on_the_queue(self):
        self.station.departure_trains = deque(["Sofia"])

        result = self.station.train_has_left("Varna")

        self.assertEqual(deque(["Sofia"]), self.station.departure_trains)

        self.assertEqual(False, result)

    def test_train_has_left_when_no_other_trains(self):
        self.station.departure_trains = deque(["Sofia"])

        result = self.station.train_has_left("Sofia")

        self.assertEqual(True, result)

        self.assertEqual(deque([]), self.station.departure_trains)


if __name__ == "__main__":
    main()
