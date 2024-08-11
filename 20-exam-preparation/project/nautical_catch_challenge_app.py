from typing import List

from project.fish.deep_sea_fish import DeapSeaFish
from project.fish.predatory_fish import PredatoryFish
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.divers.base_diver import BaseDiver


class NauticalCatchChallengeApp:
    VALID_DIVERS = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISHES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeapSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type in self.VALID_DIVERS.keys():
            diver = self.find_diver_by_name(diver_name)

            if diver:
                return f"{diver_name} is already a participant."
            else:
                diver = self.VALID_DIVERS[diver_type](diver_name)
                self.divers.append(diver)

                return f"{diver_name} is successfully registered for the competition as a {diver_type}."
        else:
            return f"{diver_type} is not allowed in our competition."

    def find_diver_by_name(self, name):
        for diver in self.divers:
            if diver.name == name:
                return diver

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type in self.VALID_FISHES:
            fish = self.find_fish_by_name(fish_name)

            if fish:
                return f"{fish_name} is already permitted."
            else:
                fish = self.VALID_FISHES(fish_type)(fish_name)
                self.fish_list.append(fish)

                return f"{fish_name} is allowed for chasing as a {fish_type}."
        else:
            return f"{fish_type} is forbidden for chasing in our competition."

    def find_fish_by_name(self, name):
        for fish in self.fish_list:
            if fish.name == name:
                return fish

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self.find_diver_by_name(diver_name)
        fish = self.find_fish_by_name(fish_name)

        if not diver:
            return f"{diver_name} is not registered for the competition."

        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {diver.competition_points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."
        else:
            diver.hit(fish)
            return f"{diver_name} hits a {diver.competition_points}pt. {fish_name}."

    def health_recovery(self):
        pass

    def diver_catch_report(self, diver_name: str):
        pass

    def competition_statistics(self):
        pass
