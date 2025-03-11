# Get user input
user_input = input("Enter a list of integers separated by commas: ")
numbers = list(map(int, user_input.split(',')))

# Lambda functions to filter even/odd
even = list(filter(lambda x: x % 2 == 0, numbers))
odd = list(filter(lambda x: x % 2 != 0, numbers))

# Display results
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")