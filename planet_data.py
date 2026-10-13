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

MERCURY = Planet(
    name="Mercury",
    orbital_period_days=87.97,
    orbit_rank=1,
    starting_angle_rad=math.radians(252.25),
)

VENUS = Planet(
    name="Venus",
    orbital_period_days=224.70,
    orbit_rank=2,
    starting_angle_rad=math.radians(181.98),
)

EARTH = Planet(
    name="Earth",
    orbital_period_days=365.25,
    orbit_rank=3,
    starting_angle_rad=math.radians(100.46),
)

MARS = Planet(
    name="Mars",
    orbital_period_days=686.98,
    orbit_rank=4,
    starting_angle_rad=math.radians(-4.55),
)

JUPITER = Planet(
    name="Jupiter",
    orbital_period_days=4332.82,
    orbit_rank=5,
    starting_angle_rad=math.radians(34.40),
)

SATURN = Planet(
    name="Saturn",
    orbital_period_days=10755.70,
    orbit_rank=6,
    starting_angle_rad=math.radians(49.95),
)

URANUS = Planet(
    name="Uranus",
    orbital_period_days=30687.15,
    orbit_rank=7,
    starting_angle_rad=math.radians(313.24),
)

NEPTUNE = Planet(
    name="Neptune",
    orbital_period_days=60190.03,
    orbit_rank=8,
    starting_angle_rad=math.radians(-55.12),
)

PLUTO = Planet(
    name="Pluto",
    orbital_period_days=90560,
    orbit_rank=9,
    starting_angle_rad=math.radians(238.93),
)

PLANETS = [
    MERCURY,
    VENUS,
    EARTH,
    MARS,
    JUPITER,
    SATURN,
    URANUS,
    NEPTUNE,
    PLUTO
]