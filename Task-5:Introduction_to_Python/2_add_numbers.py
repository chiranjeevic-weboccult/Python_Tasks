def add_without_plus(a, b):
    """
    Add two positive integers by repeatedly incrementing/decrementing.
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: Sum of a and b
    """
    while b != 0:
        a += 1  
        b -= 1  
    return a

# Get user input
num1 = int(input("Enter first positive integer: "))
num2 = int(input("Enter second positive integer: "))

# Calculate and display result
print(f"Sum: {add_without_plus(num1, num2)}")