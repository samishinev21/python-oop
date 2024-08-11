from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 120

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        reduce_amount = round(time_to_catch * 60 / 100)

        if (self.oxygen_level - reduce_amount) < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= reduce_amount

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL
