"""
This program checks if a given string is a palindrome. A palindrome is a word, phrase,
number, or sequence of characters that reads the same forward and backward (ignoring spaces
and capitalization). The user enters a string, and the program determines whether it is a
palindrome.
"""

def is_palindrome(s):
    """
    Checks if a given string is a palindrome.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is the same forwards and backwards
    return s == s[::-1]


# Allow user to input a string dynamically
user_input = input("Enter a string: ").strip()

# Check if the input string is a palindrome
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')