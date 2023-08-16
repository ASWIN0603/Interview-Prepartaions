array = [1,2,3,4,5,5,3,2,5,3,2,1,9,6]
new_array = []
for x in array :
    if x not in new_array:
       new_array.append(x)
print(sorted(new_array))