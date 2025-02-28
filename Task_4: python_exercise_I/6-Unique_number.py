"""
This program checks if all numbers in a given list are unique. The user enters numbers
separated by commas, and the program determines whether all numbers are unique or if there
are duplicates.
"""

def are_all_unique(numbers):
    """
    Checks if all numbers in a list are unique.

    Args:
        numbers (list): A list of integers to check for uniqueness.

    Returns:
        bool: True if all numbers are unique, False otherwise.
    """
    # Check if the length of the list matches the length of the set
    return len(numbers) == len(set(numbers))


# Allow user to input numbers dynamically
user_input = input("Enter numbers separated by commas (e.g., 1, 2, 3, 4): ").strip()

try:
    # Convert the input string into a list of integers
    numbers = [int(num.strip()) for num in user_input.split(",")]

    # Check if all numbers are unique
    result = are_all_unique(numbers)

    # Print the result
    if result:
        print("All numbers are unique.")
    else:
        print("There are duplicate numbers.")

except ValueError:
    print("Invalid input. Please enter numbers separated by commas.")