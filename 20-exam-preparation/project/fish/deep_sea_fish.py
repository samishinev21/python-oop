from project.fish.base_fish import BaseFish


class DeapSeaFish(BaseFish):
    TIME_TO_CATCH = 180

    def __init__(self, name: str, points: float):
        super().__init__(name, points, DeapSeaFish.TIME_TO_CATCH)

    def fish_details(self):
        return (f"{self.__class__.__name__}: {self.name}"
                f" [Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]")
