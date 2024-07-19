from unittest import TestCase, main
from list import IntegerList

class TestList(TestCase):
    def setUp(self):
        self.list = IntegerList(10, 3.14, 6, 5, 7.36)

    def test_init(self):
        self.assertEqual([10, 6, 5], self.list.get_data())

    def test_get_data_returns_expected_elements(self):
        self.assertEqual([10, 6, 5], self.list.get_data())

    def test_add_appends_new_elements(self):
        self.list.add(1)

        self.assertEqual([10, 6, 5, 1], self.list.get_data())

    def test_add_allows_only_integers(self):
        with self.assertRaises(Exception) as ex:
            self.list.add(3.14)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_removes_element_index(self):
        result = self.list.remove_index(0)
        expected_integers = [6, 5]

        self.assertEqual(10, result)
        self.assertEqual(expected_integers, self.list.get_data())

    def test_remove_element_raises_error_on_index_out_of_range(self):
        with self.assertRaises(Exception) as ex:
            self.list.remove_index(15)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_returns_the_expected_element(self):
        result = self.list.get(0)

        self.assertEqual(10, result)

    def test_get_raises_error_on_index_out_of_range(self):
        with self.assertRaises(Exception) as ex:
            self.list.get(10)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_adds_new_element_to_the_list(self):
        self.list.insert(0, 0)

        self.assertEqual([0, 10, 6, 5], self.list.get_data())

    def test_insert_raises_error_on_index_out_of_range(self):
        with self.assertRaises(Exception) as ex:
            self.list.insert(1000, 0)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_raises_error_on_none_integer(self):
        with self.assertRaises(Exception) as ex:
            self.list.insert(0, "ojrk")
        
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_biggest_num(self):
        self.assertEqual(10, self.list.get_biggest())

    def test_index(self):
        self.assertEqual(0, self.list.get_index(10))

if __name__ == "__main__":

    main()