from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Samuel", 21, 100, 15)

    def test_init(self):
        self.assertEqual("Samuel", self.hero.username)
        self.assertEqual(21, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(15, self.hero.damage)

    def test_error_when_you_are_fighting_yourself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_error_when_health_less_than_zero(self):
        self.hero.health = -10
        enemy_hero = Hero("Haralampi", 21, 10, 15)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_if_enemy_health_low_error(self):
        enemy_hero = Hero("Jackson", 21, -10, 15)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual("You cannot fight Jackson. He needs to rest", str(ex.exception))

    def test_battle_when_draw(self):
        enemy_hero = Hero("Jackson", 21, 100, 15)
        result = self.hero.battle(enemy_hero)

        self.assertEqual("Draw", result)

    def test_battle_result_you_win(self):
        self.hero.health = 10000
        enemy_hero = Hero("Lebron", 21, 100, 15)

        result = self.hero.battle(enemy_hero)

        self.assertEqual("You win", result)

    def test_battle_result_you_lose(self):
        enemy_hero = Hero("Mira", 21, 10000, 15)
        result = self.hero.battle(enemy_hero)

        self.assertEqual("You lose", result)

    def test_string(self):
        self.assertEqual(
            "Hero Samuel: 21 lvl\nHealth: 100\nDamage: 15\n",
            str(self.hero)
        )


if __name__ == "__main__":
    main()
