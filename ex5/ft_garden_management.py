#!/usr/bin/env python3

class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised when a specific plant issue is detected."""
    pass


class WaterError(GardenError):
    """Raised when irrigation is compromised."""
    pass


class GardenManager:
    """Manages garden plants and performs safety checks."""

    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, name: str, water: int = 5, sun: int = 8) -> None:
        """Add a plant to the garden with basic validation."""
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append({"name": name, "water": water, "sun": sun})
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        """Water all plants in the garden."""
        print("Watering plants...")
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant['name']} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self) -> None:
        print("Checking plant health...")
        for plant in self.plants:
            try:
                if plant["water"] > 10:
                    raise WaterError(
                        f"Water level {plant['water']} is too high (max 10)"
                    )
                print(
                    f"{plant['name']}: healthy "
                    f"(water: {plant['water']}, sun: {plant['sun']})"
                )
            except GardenError as e:
                print(f"Error checking {plant['name']}: {e}")


def test_garden_system() -> None:
    """Test the garden management system with error handling."""
    manager = GardenManager()

    print("=== Garden Management System ===")
    print()

    print("Adding plants to garden...")
    for plant in [
        ("tomato", 5, 8),
        ("lettuce", 15, 8),
        ("", 5, 5),
    ]:
        try:
            manager.add_plant(*plant)
        except PlantError as e:
            print(f"Error adding plant: {e}")

    print()
    manager.water_plants()
    print()

    manager.check_health()
    print()

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
        print("System recovered and continuing...")

    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_system()
