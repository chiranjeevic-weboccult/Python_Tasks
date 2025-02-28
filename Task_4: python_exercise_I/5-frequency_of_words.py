"""
This program calculates the frequency of each word in a given text. It removes punctuation,
converts all words to lowercase, and counts the occurrences of each word using the Counter
class from the collections module. The user can input any text, and the program will display
the word frequencies.
"""

from collections import Counter
import re


def count_word_frequencies(text):
    """
    Counts the frequency of each word in the given text.

    Args:
        text (str): The input text to analyze.

    Returns:
        dict: A dictionary where keys are words and values are their respective frequencies.
    """
    # Replace punctuation with spaces (except apostrophes within words)
    cleaned_text = re.sub(r"[^\w\s']", ' ', text)

    # Convert to lowercase and split into words
    words = cleaned_text.lower().split()

    # Count word frequencies using Counter
    return dict(Counter(words))


# Allow user to input text dynamically
text = input("Enter your text: ").strip()  # Remove leading/trailing spaces

# Calculate word frequencies
word_frequencies = count_word_frequencies(text)

print("Word Frequencies:", word_frequencies)