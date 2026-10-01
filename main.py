from datetime import datetime
from input_helpers import prompt_for_output_path, prompt_for_input, stage_header
from planet_data import REFERENCE_DATE, EARTH
from orbital_math import calculate_orbital_angle, calculate_position
from plaque_conversion import calculate_plaque_radius
from visualization import plot_positions
from mesh_generation import create_plaque

def main():
    OUTPUT_PATH = prompt_for_output_path()

    loop = True
    # Print header
    stage_header("Welcome to Planet Plotter!")

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

    stage_header(f"Calculating days since {target_date}")

    days_elapsed = (target_date - REFERENCE_DATE).days
    
    stage_header("Calculating Earth's orbital angle")

    earth_orbit_angle = calculate_orbital_angle(EARTH, days_elapsed)
    
    stage_header("Calculating Earth's position on plaque")

    earth_radius = calculate_plaque_radius(EARTH.orbit_rank)
    earth_pos = calculate_position(earth_radius, earth_orbit_angle)

    print("Days: ", days_elapsed)
    print("Orbital Angle: ", earth_orbit_angle)
    print(f"Orbit Position: {earth_pos}")

    stage_header("Rendering visual map (Close window to continue)")

    plot_positions([("Earth", earth_pos[0], earth_pos[1])])

    stage_header("Rendering test STL file")

    create_plaque(OUTPUT_PATH, target_date)


if __name__ == "__main__":
    main()