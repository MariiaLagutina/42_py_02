#!/usr/bin/env python3

def garden_operations() -> None:
    """
    Demonstrates handling of various Python built-in exceptions
    using try/except blocks, while keeping the program running.
    """
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print()

    print("Testing ZeroDivisionError...")
    try:
        _ = 1 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print()

    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print()

    print("Testing KeyError...")
    try:
        d = {}
        _ = d["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print()

    print("Testing multiple errors together...")
    try:
        int("xyz")  # Will raise ValueError
        _ = 1 / 0   # Won't execute because previous line fails
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")
    print()


def test_error_types() -> None:
    """
    Runs all error-handling demonstrations and shows that
    the program continues execution after each error.
    """
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
