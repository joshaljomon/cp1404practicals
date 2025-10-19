"""
Word Occurrences
Estimate: 15 mins
Actual: 23 mins
"""

word_to_count = {}
text = input("Text: ").lower()
words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

max_length = max(len(word) for word in words)
for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")