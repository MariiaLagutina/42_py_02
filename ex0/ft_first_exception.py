#!/usr/bin/env python3

def check_temperature(temp_str) -> int | None:
    """
    Validates if the input string is a valid number and within
    the agricultural safety range (0-40°C).
    """
    try:
        temperature = int(temp_str)

        if 0 <= temperature <= 40:
            print(f"Temperature {temperature}°C is perfect for plants!")
            return temperature
        elif temperature > 40:
            print(f"Error: {temperature}°C is too hot for plants (max 40°C)")
        else:
            print(f"Error: {temperature}°C is too cold for plants (min 0°C)")

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")

    return None


def test_temperature_input() -> None:
    """
    Demonstrates the temperature validation pipeline with various inputs
    to ensure the program handles errors without crashing.
    """
    print("=== Garden Temperature Checker ===")

    test_values = ["25", "abc", "100", "-50"]

    for val in test_values:
        print()
        print(f"Testing temperature: {val}")
        check_temperature(val)

    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
