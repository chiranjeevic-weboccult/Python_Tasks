import math

def common_divisors(a, b):
    """
    Find all common divisors of two numbers.
    
    Args:
        a (int): First number.
        b (int): Second number.
    
    Returns:
        list: List of common divisors.
    """
    gcd_value = math.gcd(a, b)
    return [i for i in range(1, gcd_value + 1) if gcd_value % i == 0]

# Get user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Compute and display divisors
print(f"Common divisors of {num1} and {num2}: {common_divisors(num1, num2)}")