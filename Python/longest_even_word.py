# Return the Longest Word with even Length 

sentence = "hello there is a pipe"

splitted_sentence = sentence.split()
print(splitted_sentence)
length_array = []
for words in splitted_sentence:
    length_array.append(len(words))
print(length_array)
index = 0
for i in range(0,len(length_array)):
    
    if length_array[i] % 2 == 0 and length_array[index] < length_array[i] :
        index = i
print(splitted_sentence[index])