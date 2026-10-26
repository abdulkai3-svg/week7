"""Process a list of numbers and a list of words, then print the results."""

# Words longer than this get uppercased, shorter ones get lowercased
LONG_WORD_LENGTH = 5


def process_numbers(numbers):
    """Double even numbers and triple odd numbers.

    Args:
        numbers (list of int): The numbers to process.

    Returns:
        list of int: A new list with each number doubled or tripled.
    """
    return [num * 2 if num % 2 == 0 else num * 3 for num in numbers]


def process_strings(words):
    """Uppercase long words and lowercase short words.

    Args:
        words (list of str): The words to format.

    Returns:
        str: The formatted words joined into one string with spaces.
    """
    formatted_words = [
        word.upper() if len(word) > LONG_WORD_LENGTH else word.lower()
        for word in words
    ]
    # join() handles the spacing so there's no trailing space to strip
    return " ".join(formatted_words)


def main():
    """Run both processing functions on sample data and print the results."""
    numbers = [1, 2, 3, 4, 5, 6, 7]
    fruits = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_numbers = process_numbers(numbers)
    processed_fruits = process_strings(fruits)

    print("Processed Numbers:", processed_numbers)
    print("Processed Strings:", processed_fruits)


if __name__ == "__main__":
    main()