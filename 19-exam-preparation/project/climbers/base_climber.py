from abc import ABC, abstractmethod


class BaseClimber(ABC):
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
        self.conquered_peaks = []
        self.is_prepared = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Climber name cannot be null or empty")

        self.name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength equal to 0!")

        self.strength = value

    @abstractmethod
    def can_climb(self):
        pass

    @abstractmethod
    def climb(self, peak):
        pass

    def rest(self):
        self.strength += 15

    def __str__(self):
        result = f"{self.__class__.__name__}: /// Climber name: {self.name} * Left strength: {self.strength:.1f} * "
        result += f"Conquered peaks: {', '.join(self.conquered_peaks)}"
        return result
