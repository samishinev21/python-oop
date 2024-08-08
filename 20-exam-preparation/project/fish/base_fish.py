from abc import ABC, abstractmethod


class BaseFish(ABC):
    def __init__(self, name: str, points: float, time_to_catch: int):
        self.name = name
        self.points = points
        self.time_to_catch = time_to_catch

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Fish name should be determined!")

        self.__name = value

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        if 1 < value > 10:
            raise ValueError("Points should be a value ranging from 1 to 10!")

        self.__points = value

    @property
    def time_to_catch(self):
        return self.__time_to_catch

    @time_to_catch.setter
    def time_to_catch(self, value):
        self.__time_to_catch = value

    @abstractmethod
    def fish_details(self):
        pass
