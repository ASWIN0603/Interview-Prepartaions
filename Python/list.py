

# List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single, readable line.

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words  if word not in ('the', 'over')]
print(words)
print(word_lengths)


arr = [1, 2, 3, -4, -3, 2, -5, -1, 3, 6]
new_arr = [num for num in arr if num >= 0 ]
print('duplicate_elements_removed_array',new_arr)
