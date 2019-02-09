from datetime import timedelta, datetime
from math import hypot

from village import Village


class Attack:

    def __init__(self, attacker: Village, target: Village,
                 unit_speed: timedelta, arrive_time: datetime) -> None:
        self.attacker = attacker
        self.target = target
        self.unit_speed = unit_speed
        self.arrive_time = arrive_time

    @property
    def distance(self):
        return hypot(
            self.attacker.x - self.target.x,
            self.attacker.y - self.target.y
        )

    @property
    def duration(self):
        return self.distance * self.unit_speed

    @property
    def attack_at(self):
        return self.arrive_time - self.duration
