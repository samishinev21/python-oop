from project.climbing_robot import ClimbingRobot
from unittest import TestCase, main


class TestClimbingRobot(TestCase):
    def setUp(self):
        self.robot = ClimbingRobot("Indoor", "Part", 100, 100)

    def test_init(self):
        self.assertEqual("Indoor", self.robot.category)
        self.assertEqual("Part", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(100, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_category_setter_valid(self):
        self.robot.category = "Mountain"

        self.assertEqual(self.robot.category, "Mountain")

    def test_category_setter_invalid(self):
        with self.assertRaises(ValueError) as error:
            self.robot.category = "invalid"

        self.assertEqual(f"Category should be one of {self.robot.ALLOWED_CATEGORIES}", str(error.exception))

    def test_get_used_capacity(self):
        self.robot.installed_software = [
            {"capacity_consumption": 10, "memory_consumption": 10},
            {"capacity_consumption": 10, "memory_consumption": 10}
        ]

        self.assertEqual(20, self.robot.get_used_capacity())

    def test_get_used_memory(self):
        self.robot.installed_software = [
            {"capacity_consumption": 10, "memory_consumption": 10},
            {"capacity_consumption": 10, "memory_consumption": 10}
        ]

        self.assertEqual(20, self.robot.get_used_memory())

    def test_get_available_capacity(self):
        self.robot.installed_software = [
            {"capacity_consumption": 10, "memory_consumption": 10},
            {"capacity_consumption": 10, "memory_consumption": 10}
        ]

        self.assertEqual(80, self.robot.get_available_capacity())

    def test_get_available_memory(self):
        self.robot.installed_software = [
            {"capacity_consumption": 10, "memory_consumption": 10},
            {"capacity_consumption": 10, "memory_consumption": 10}
        ]

        self.assertEqual(80, self.robot.get_available_memory())

    def test_install_software_succeed_when_available_memory_and_consumption(self):
        result = self.robot.install_software({"name": "ROS", "capacity_consumption": 10, "memory_consumption": 10})

        self.assertEqual([{"name": "ROS", "capacity_consumption": 10, "memory_consumption": 10}],
                         self.robot.installed_software)
        self.assertEqual("Software 'ROS' successfully installed on Indoor part.", result)

    def test_install_software_fails_when_not_available_capacity(self):
        result = self.robot.install_software({"name": "ROS", "capacity_consumption": 120, "memory_consumption": 10})

        self.assertEqual(f"Software 'ROS' cannot be installed on Indoor part.", result)

    def test_install_software_fails_when_not_available_memory(self):
        result = self.robot.install_software({"name": "ROS", "memory_consumption": 120, "capacity_consumption": 10})

        self.assertEqual(f"Software 'ROS' cannot be installed on Indoor part.", result)


if __name__ == "__main__":
    main()
