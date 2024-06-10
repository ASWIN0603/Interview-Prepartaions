array = [2,3,4,1,2,3,1,4,4,7,2,3,4,1]
max_count = 0
index = 0
length = len(array)
print(length,"length of the array")

for i in range(0,length):
    count = 0
    for j in range(0,length):
        if array[i] == array[j]:
            count = count +1
    if count > max_count :
        index = i
        max_count = count
print("last index of the most repeated numebr ", i)
print("most repeated numebr", array[index])
print("time the most repeated number occurs",max_count)


array = [2,3,4,1,2,3,1,4,4,7,2,3,4,1]
unique_set = set(array)
print(unique_set)
max_count = 0
index = 0
for i in unique_set:
    count = 0
    for j in array:
        if i == j:
            count += 1
    if count > max_count:
        max_count = count
        index = i
print (index, max_count)

