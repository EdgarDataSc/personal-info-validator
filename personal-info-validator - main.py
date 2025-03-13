def get_validated_input(prompt, data_type):
    """
    Function to get user input and validate its type.
    :param prompt: The input message to display.
    :param data_type: The expected data type (int, float, str).
    :return: Validated user input.
    """
    while True:
        try:
            value = input(prompt)
            if data_type == int:
                return int(value)
            elif data_type == float:
                return float(value)
            else:
                return value.strip()
        except ValueError:
            print(f"Invalid input! Please enter a valid {data_type.__name__}.")


def main():
    print("\n--- User Information Validator ---\n")

    # Get user details
    name = get_validated_input("Enter your name: ", str)
    age = get_validated_input("Enter your age: ", int)
    weight = get_validated_input("Enter your weight (kg): ", float)

    # Display user details
    print("\n--- User Information ---")
    print(f"Name: {name}")
    print(f"Age: {age} years old")
    print(f"Weight: {weight:.2f} kg")

    # Simple validation
    if age < 18:
        print("\nYou are under 18. Parental guidance may be required.")
    else:
        print("\nYou are an adult.")

    print("\nThank you for using the Personal Information Validator!\n")


if __name__ == "__main__":
    main()
