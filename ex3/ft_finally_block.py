#!/usr/bin/env python3

def water_plants(plant_list) -> None:
    """
    Waters each plant in the list and ensures the system is always closed.

    Args:
        plant_list (list): A list of plant names as strings.
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """
    Tests the watering system with both valid and invalid plant lists.
    """
    print("=== Garden Watering System ===")
    print()

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")
    print()

    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
