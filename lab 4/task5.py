import string

def most_frequent_word(paragraph):
    # Convert to lowercase
    paragraph = paragraph.lower()
    # Remove punctuation
    paragraph = paragraph.translate(str.maketrans('', '', string.punctuation))
    # Split into words
    words = paragraph.split()
    # Count word frequency
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    # Find the most frequent word
    most_freq = max(freq, key=freq.get)
    return most_freq

# Example usage:
if __name__ == "__main__":
    text = "SR University, located in Warangal, Telangana, is a leading institution known for its innovation-driven education. It offers a wide range of programs in engineering, management, and sciences, fostering research and entrepreneurship. With modern infrastructure and skilled faculty, SR University provides students with opportunities to excel globally."
    print("Most frequent word:", most_frequent_word(text))
