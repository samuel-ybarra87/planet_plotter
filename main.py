from datetime import datetime, date

def validate_length(value: str, length: str) -> str:
    if "-" in value:
        raise Exception(f"No negative numbers...")

    if(length == "YYYY"):
        valid_length = 4
    else:
        valid_length = 2

    digit_length = len(value)

    if(digit_length < valid_length) or (digit_length > valid_length):
        raise Exception(f"Follow exact format - {length}")

    return value

def prompt_for_input(promt_text: str, length="YYYY") -> str:
    while True:
        raw_value = input(promt_text)
        try:
            return validate_length(raw_value, length)
        except Exception as err:
            print(f"{err.args[0]}")

def main():
    loop = True
    # Print header
    print("******************************")
    print("Welcome to Planet Plotter!")
    print("******************************")

    while loop:
        year = prompt_for_input("Enter a target year: ")
        month = prompt_for_input("Enter a target month: ", "MM")
        day = prompt_for_input("Enter a target day: ", "DD")
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

    days_elapsed = (date.today() - target_date).days

    print("Days: ", days_elapsed)



if __name__ == "__main__":
    main()