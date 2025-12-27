#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    """
    Validates plant health parameters and raises ValueError
    when any input value is invalid.
    """
    min_water_level = 1
    max_water_level = 10
    min_sunlight_hours = 2
    max_sunlight_hours = 12

    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level < min_water_level:
        raise ValueError(f"Water level {water_level} is too low "
                         f"(min {min_water_level})")
    elif water_level > max_water_level:
        raise ValueError(f"Water level {water_level} is too high "
                         f"(max {max_water_level})")

    if sunlight_hours < min_sunlight_hours:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low "
                         f"(min {min_sunlight_hours})")
    elif sunlight_hours > max_sunlight_hours:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high "
                         f"(max {max_sunlight_hours})")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """Tests various health check scenarios."""
    print("=== Garden Plant Health Checker ===")
    print()

    print("Testing good values...")
    print(check_plant_health("tomato", 5, 8))
    print()

    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print('Testing bad water level...')
    try:
        check_plant_health("Rose", 15, 5)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("Tulip", 8, 1)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
