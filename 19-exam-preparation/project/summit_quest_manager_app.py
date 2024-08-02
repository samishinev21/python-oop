from climbers.arctic_climber import ArcticClimber
from climbers.base_climber import BaseClimber
from climbers.summit_climber import SummitClimber
from peaks.base_peak import BasePeak
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

    def check_gear(self, climber_name: str, peak_name: str, gear: []):
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

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self.find_climber_by_name(climber_name)
        peak = self.find_peak_by_name(peak_name)

        if climber is None:
            return f"Climber {climber_name} is not registered yet."

        if peak is None:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.is_prepared and climber.can_climb():
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        climbed_peaks = set()
        climbed_climbers = []

        for climber in self.climbers:
            if len(climber.conquered_peaks) > 0:
                climbed_climbers.append(climber)
                for peak in climber.conquered_peaks:
                    climbed_peaks.add(peak)

        result = f"Total climbed peaks: {len(climbed_peaks)}\n"
        result += "**Climber's statistics:**"
        sorted_climbers = sorted(climbed_climbers, key=lambda clm: (-len(clm.conquered_peaks), clm.name))
        for climber in sorted_climbers:
            result += f"\n{str(climber)}"

        return result

    def find_climber_by_name(self, name) -> BaseClimber:
        for climber in self.climbers:
            if climber.name == name:
                return climber

    def find_peak_by_name(self, name) -> BasePeak:
        for peak in self.peaks:
            if peak.name == name:
                return peak


climbing_app = SummitQuestManagerApp()

# Register climbers
print(climbing_app.register_climber("ArcticClimber", "Alice"))
print(climbing_app.register_climber("SummitClimber", "Bob"))
print(climbing_app.register_climber("ExtremeClimber", "Dave"))
print(climbing_app.register_climber("ArcticClimber", "Charlie"))
print(climbing_app.register_climber("ArcticClimber", "Alice"))
print(climbing_app.register_climber("SummitClimber", "Eve"))
print(climbing_app.register_climber("SummitClimber", "Frank"))

# Add peaks to the wish list
print(climbing_app.peak_wish_list("ArcticPeak", "MountEverest", 4000))
print(climbing_app.peak_wish_list("SummitPeak", "K2", 3000))
print(climbing_app.peak_wish_list("ArcticPeak", "Denali", 2500))
print(climbing_app.peak_wish_list("UnchartedPeak", "MysteryMountain", 2000))

# Prepare climbers for climbing
print(climbing_app.check_gear("Alice", "MountEverest", ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]))
print(climbing_app.check_gear("Bob", "K2", ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]))
print(climbing_app.check_gear("Charlie", "Denali", ["Ice axe", "Crampons"]))

# Perform climbing
print(climbing_app.perform_climbing("Alice", "MountEverest"))
print(climbing_app.perform_climbing("Bob", "K2"))
print(climbing_app.perform_climbing("Kelly", "Denali"))
print(climbing_app.perform_climbing("Alice", "K2"))
print(climbing_app.perform_climbing("Alice", "MysteryMountain"))
print(climbing_app.perform_climbing("Eve", "MountEverest"))
print(climbing_app.perform_climbing("Charlie", "MountEverest"))
print(climbing_app.perform_climbing("Frank", "K2"))
print(climbing_app.perform_climbing("Frank", "Denali"))
print(climbing_app.perform_climbing("Frank", "MountEverest"))

# Get statistics
print(climbing_app.get_statistics())
