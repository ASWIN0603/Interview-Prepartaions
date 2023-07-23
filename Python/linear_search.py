#linear search
def linear_search(arr,number_to_find):
    length = len(arr)
    for i in range (0,length):
        if arr[i] == number_to_find:
            return (f"The element is present at index {i}")
        
    return 'Item not Found'

arr = []
arr_length = int(input('Enter the length of the Array:'))
for i in range(0,arr_length):
    element = int(input(f"Enter the {'last' if i ==(arr_length-1) else i+1} element:"))
    arr.append(element)
number_to_find = int(input('Enter the number to find:'))

result=linear_search(arr,number_to_find)
print (result)