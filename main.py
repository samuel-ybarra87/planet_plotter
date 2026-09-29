from datetime import datetime
from input_helpers import prompt_for_input
from planet_data import REFERENCE_DATE, EARTH
from orbital_math import calculate_orbital_angle, calculate_position
from plaque_conversion import calculate_plaque_radius

def main():
    loop = True
    # Print header
    print("******************************")
    print("Welcome to Planet Plotter!")
    print("******************************")

    while loop:
        year = prompt_for_input("Enter a target year (YYYY): ")
        month = prompt_for_input("Enter a target month (MM): ", "MM")
        day = prompt_for_input("Enter a target day (DD): ", "DD")
        try:
            date_string = f"{year}-{month}-{day}"
            target_date = datetime.strptime(date_string, "%Y-%m-%d").date()
            loop = False
        except ValueError as err:
            print("That is not a valid date.")
            print(f"{err.args[0]}")

    print("******************************")
    print(f"Calculating days since {target_date}")
    print("******************************")

    days_elapsed = (target_date - REFERENCE_DATE).days
    
    print("******************************")
    print(f"Calculating Earth's orbital angle")
    print("******************************")

    earth_orbit_angle = calculate_orbital_angle(EARTH, days_elapsed)
    
    print("******************************")
    print(f"Calculating Earth's position on plaque")
    print("******************************")

    earth_radius = calculate_plaque_radius(EARTH.orbit_rank)
    earth_pos = calculate_position(earth_radius, earth_orbit_angle)

    print("Days: ", days_elapsed)
    print("Orbital Angle: ", earth_orbit_angle)
    print(f"Orbit Position: {earth_pos}")



if __name__ == "__main__":
    main()