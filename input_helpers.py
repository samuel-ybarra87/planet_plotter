import os

def prompt_for_output_path() -> str:
    while True:
        raw_path = input("Enter output folder path for the STL file: ")
        if not raw_path:
            return ""
        if not os.path.isdir(raw_path):
            if os.path.isfile(raw_path):
                print("That's a file, not a directory...")
                continue

            answer = input("Not a valid path. Create? (Y/N): ")
            if answer != "Y":
                print("Exiting")
                exit(0)
            else:
                try:
                    os.makedirs(raw_path)
                    return raw_path
                except FileExistsError:
                    print("Could not create directory. Try again...")
        else:
            print("STL files will be stored here\n")
            return raw_path

def stage_header(title: str) -> str:
    banner_top = ""
    banner_bottom = ""
    for i in range(0, len(title)):
        banner_top += "*"
        banner_bottom += "*"

    print(banner_top)
    print(title)
    print(banner_bottom)

def validate_length(value: str, length: str) -> str:
    if "-" in value:
        raise Exception(f"No negative numbers...")

    if(length == "YYYY"):
        valid_length = 4
    else:
        valid_length = 2

    digit_length = len(value)

    if(digit_length < valid_length) or (digit_length > valid_length):
        raise ValueError(f"Follow exact format - {length}")

    return value

def prompt_for_input(promt_text: str, length="YYYY") -> str:
    while True:
        raw_value = input(promt_text)
        try:
            return validate_length(raw_value, length)
        except ValueError as err:
            print(f"{err.args[0]}")
        except Exception as err:
            print(f"{err.args[0]}")