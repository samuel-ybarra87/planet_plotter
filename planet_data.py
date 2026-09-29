from datetime import date
from dataclasses import dataclass
import math

REFERENCE_DATE = date(2000, 1, 1)

@dataclass
class Planet:
    name: str
    orbital_period_days: float
    orbit_rank: int
    starting_angle_rad: float

EARTH = Planet(
    name="Earth",
    orbital_period_days=365.25,
    orbit_rank=3,
    starting_angle_rad=math.radians(100.46),
)