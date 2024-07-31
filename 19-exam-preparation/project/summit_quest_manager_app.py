from typing import List

from climbers.arctic_climber import ArcticClimber
from climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    CLIMBER_TYPES = ["ArcticClimber", "SummitClimber"]
    PEAK_TYPES = ["ArcticPeak", "SummitPeak"]

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."

        climber = self.find_climber_by_name(climber_name)
        if climber:
            return f"{climber_name} has been already registered."

        if climber_type == "ArcticClimber":
            self.climbers.append(ArcticClimber(climber_name))

        elif climber_type == "SummitClimber":
            self.climbers.append(SummitClimber(climber_name))

        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.PEAK_TYPES:
            return f"{peak_type} is an unknown type of peak."

        if peak_type == "ArcticPeak":
            peak = ArcticPeak(peak_name, peak_elevation)
            self.peaks.append(peak)

        elif peak_type == "SummitPeak":
            peak = SummitPeak(peak_name, peak_elevation)
            self.peaks.append(peak)

        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        climber = self.find_climber_by_name(climber_name)
        peak = self.find_peak_by_name(peak_name)

        missing_gears = [g for g in sorted(peak.get_recommended_gear()) if g not in gear]

        if len(missing_gears) > 0:
            climber.is_prepared = False
            result = f"{climber_name} is not prepared" \
                     f" to climb {peak_name}. Missing gear: {', '.join(missing_gears)}."

            return result
        else:
            return f"{climber_name} is prepared to climb {peak_name}."

    def find_climber_by_name(self, name):
        for climber in self.climbers:
            if climber.name == name:
                return climber

    def find_peak_by_name(self, name):
        for peak in self.peaks:
            if peak.name == name:
                return peak
