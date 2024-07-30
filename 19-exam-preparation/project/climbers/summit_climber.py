from peaks.base_peak import BasePeak
from project.climbers.base_climber import BaseClimber


class SummitClimber(BaseClimber):
    def __init__(self, name, strength=150):
        super().__init__(name, strength)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Advanced":
            self.strength = self.strength - 30 * 1.3
        else:
            self.strength = self.strength - 30 * 2.5

        self.conquered_peaks.append(peak.name)
