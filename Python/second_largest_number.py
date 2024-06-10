n = int(input())
arr = list(map(int, input().split()))
new_arr = sorted(set(arr))
print(new_arr[len(new_arr)-2])