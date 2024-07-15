from unittest import TestCase, main
from cat import Cat

class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Samuel")

    def test_init(self):
        self.assertEqual("Samuel", self.cat.name)
        self.assertEqual(False, self.cat.fed)
        self.assertEqual(False, self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_cat_size_increased(self):
        self.cat.eat()

        expected = 1

        self.assertEqual(expected, self.cat.size)

    def test_fed_after_eating(self):
        self.cat.eat()

        self.assertEqual(True, self.cat.fed)

    def test_cannot_eat_after_fed(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))
    
    def test_cannot_sleep_when_not_fed(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_not_sleepy_after_sleeping(self):
        self.cat.fed = True

        self.cat.sleep()

        self.assertEqual(False, self.cat.sleepy)

if __name__ == "__main__":
    main()