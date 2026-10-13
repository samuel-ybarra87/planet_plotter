from datetime import datetime
from input_helpers import prompt_for_output_path, prompt_for_input, stage_header
from planet_data import REFERENCE_DATE
from orbital_math import calculate_orbital_angle, calculate_position
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
    
    stage_header("Compiling Planet Data")

    stage_header("Rendering test STL file")

    create_plaque(OUTPUT_PATH, target_date, days_elapsed)


if __name__ == "__main__":
    main()