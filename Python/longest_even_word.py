# Return the Longest Word with even Length 

sentence = "time to code great dddd"
index = 0
splitted_sentence = sentence.split()
length_array = []
for words in splitted_sentence:
    length_array.append(len(words))
for i in range(0,len(length_array)):
    
    if length_array[i] % 2 == 0 and length_array[index] < length_array[i] :
        index = i
print(splitted_sentence[index])