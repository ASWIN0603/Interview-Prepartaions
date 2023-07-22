def binary_search(arr,low,high,number_to_find):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == number_to_find:
            return mid
        elif arr[mid] > number_to_find:
            return binary_search(arr,low,mid-1,number_to_find)
        else :
            return binary_search(arr,mid+1,high,number_to_find)
        
    else:
        return -1
arr =[]
arr_length = int(input('Enter the length of the array:'))
for i in range(0,arr_length):
    element = int(input(f"Enter the {'last' if i == (arr_length-1) else i + 1} element: "))
    arr.append(element)
number_to_find = int(input("Enter the number to find:"))
result=binary_search(arr,0,len(arr)-1,number_to_find)
if result != -1:
    print('The Element is in the',result,'index of the array.')
else:
    print('The Element is not present')