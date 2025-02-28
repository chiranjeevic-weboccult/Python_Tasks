"""
This program calculates the factorial of a non-negative number entered by the user.
It uses an iterative approach for integers and the Gamma Function for decimal numbers.
If the user enters a negative number or invalid input, appropriate error messages are displayed.
"""

import math

def factorial(n):
    """
    Calculates the factorial of a non-negative number using an iterative approach for integers
    and the Gamma Function for decimal numbers.

    Args:
        n (float): The number for which the factorial is to be calculated.

    Returns:
        float: The factorial of the input number if it is non-negative.
        str: An error message if the input is negative.
    """
    # Handle negative numbers
    if n < 0:
        return "Factorial is not defined for negative numbers."

    # If the number is an integer, calculate factorial iteratively
    if isinstance(n, int) or n.is_integer():
        result = 1
        for i in range(1, int(n) + 1):
            result *= i
        return result

    # If the number is a decimal, use the Gamma Function
    return math.gamma(n + 1)

# Allow user to input a number dynamically
try:
    user_input = float(input("Enter a non-negative number (integers or decimals) to calculate its factorial: ").strip())

    # Calculate the factorial
    factorial_result = factorial(user_input)

    # Print the result or error message
    if isinstance(factorial_result, str):
        print(factorial_result)
    else:
        print(f"Factorial of {user_input}: {factorial_result:.6f}")

except ValueError:
    print("Invalid input. Please enter a valid non-negative number.")