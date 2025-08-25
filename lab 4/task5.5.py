import re
from collections import Counter
from typing import Optional


def most_frequent_word(text: str) -> Optional[str]:
    """
    Return the most frequently used word in the given paragraph.
    - Converts to lowercase
    - Removes punctuation
    - Splits on whitespace
    - In case of ties, returns the lexicographically smallest word
    - Returns None if no words are found
    """
    cleaned = re.sub(r"[^a-z0-9\s]", " ", text.lower())
    words = [word for word in cleaned.split() if word]

    if not words:
        return None

    word_counts = Counter(words)
    max_frequency = max(word_counts.values())
    top_words = [word for word, count in word_counts.items() if count == max_frequency]
    return min(top_words)


if __name__ == "__main__":
    try:
        paragraph = input().strip()
    except EOFError:
        paragraph = ""

    result = most_frequent_word(paragraph)
    print(result if result is not None else "")


