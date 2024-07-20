from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Samuel", "normal", "whistle")

    def test_init(self):
        self.assertEqual("Samuel", self.mammal.name)
        self.assertEqual("normal", self.mammal.type)
        self.assertEqual("whistle", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound(self):
        self.assertEqual("Samuel makes whistle", self.mammal.make_sound())

    def test_info(self):
        self.assertEqual("Samuel is of type normal", self.mammal.info())


if __name__ == "__main__":
    main()
