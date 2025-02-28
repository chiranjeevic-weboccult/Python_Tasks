"""
This program filters words from user input that start with vowels (a, e, i, o, u).
The user can enter words separated by spaces or commas. The program processes the input,
removes extra spaces, and identifies words that begin with vowels. The filtered words are
then displayed as output.
"""

def filter_vowel_words(words):
    """
    Filters words that start with vowels (a, e, i, o, u).

    Args:
        words (list): A list of words to be filtered.

    Returns:
        list: A list of words that start with vowels.
    """
    vowels = ('a', 'e', 'i', 'o', 'u')
    # Filter words that start with a vowel
    return [word for word in words if word.lower().startswith(vowels)]

# Allow user to input words dynamically
user_input = input("Enter words separated by spaces or commas: ")

# Process the input into a list of words
words_list = [word.strip() for word in user_input.replace(',', ' ').split()]

# Filter words starting with vowels
final_words = filter_vowel_words(words_list)

# Print the result
print("Words starting with a vowel:", final_words)