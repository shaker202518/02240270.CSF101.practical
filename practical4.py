def read_file(filename):               #anything inside the bracket is called parameter
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('sample.txt')
print(content[:250])  # Print the first 250 characters

def count_lines(content):                #anything inside the bracket is called parameter
    return len(content.split('\n'))

# Test the function
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

def count_words(content):
    return len(content.split())

# Test the function
num_words = count_words(content)
print(f"Number of words: {num_words}")


from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

import re
from collections import Counter

def preprocess_text(text):
    """Converts text to lowercase and removes punctuation."""
    return re.findall(r'\b\w+\b', text.lower())

def count_unique_words(words):
    """Counts the number of unique words in the text."""
    return len(set(words))

def find_longest_word(words):
    """Finds the longest word in the text."""
    return max(words, key=len) if words else ""

def count_word_occurrences(words, target):
    """Counts occurrences of a specific word (case-insensitive)."""
    return words.count(target.lower())

def percentage_longer_than_average(words):
    """Calculates the percentage of words longer than the average length."""
    if not words:
        return 0
    avg_length = sum(len(word) for word in words) / len(words)
    longer_words = [word for word in words if len(word) > avg_length]
    return (len(longer_words) / len(words)) * 100

# Example usage
text = "This is an example sentence. This sentence has some repeated words, words, words!"
words = preprocess_text(text)

target_word = "sentence"

print("Number of unique words:", count_unique_words(words))
print("Longest word:", find_longest_word(words))
print(f"Occurrences of '{target_word}':", count_word_occurrences(words, target_word))
print("Percentage of words longer than the average length:", percentage_longer_than_average(words))


# Test the function
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")


def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Test the function
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")

# Run the analysis
analyze_text('sample.txt')

def unique_words(content):
    words= content.split()