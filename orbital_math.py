from planet_data import Planet
import math

def calculate_orbital_angle(planet: Planet, days_elapsed: int) -> float:
    fraction_of_orbit = days_elapsed / planet.orbital_period_days
    angle = planet.starting_angle_rad + fraction_of_orbit * 2 * math.pi

    return angle

def calculate_position(radius: float, angle_rad: float) -> tuple[float, float]:
    x = radius * math.cos(angle_rad)
    y = radius * math.sin(angle_rad)

    return x,y