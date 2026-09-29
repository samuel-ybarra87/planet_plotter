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