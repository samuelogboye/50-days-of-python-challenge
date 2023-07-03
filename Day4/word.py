#!/usr/bin/python3

def word_index(words):
    longest_word_index = 0
    longest_word_length = 0

    for i, word in enumerate(words):
        if len(word) > longest_word_length:
            longest_word_length = len(word)
            longest_word_index = i

    for word in words:
        if len(word) == longest_word_length and words.index(word) != longest_word_index:
            return 0

    return longest_word_index


words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]
print(word_index(words1))
print(word_index(words2))
