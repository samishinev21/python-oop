from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    def __init__(self, name, strength=200):
        super().__init__(name, strength)

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength = self.strength - 20 * 2
        else:
            self.strength = self.strength - 20 * 1.5

        self.conquered_peaks.append(peak.name)

    def can_climb(self):
        return self.strength >= 100
