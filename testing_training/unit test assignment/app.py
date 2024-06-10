# sample 1
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


# sample 2
def is_even(n):
    return n % 2 == 0

#sample 3
def concatenate_strings(a, b):
    return a + b



# sample 4
def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            count += 1
    return count


# executing all the functions with sample inputs and adding try-except blocks
try:
    result_sample_1 = is_prime(3)
    print("Sample 1 Result:", result_sample_1)
except Exception as e:
    print("Error in Sample 1:", e)

try:
    result_sample_2 = is_even(-4.2)
    print("Sample 2 Result:", result_sample_2)
except Exception as e:
    print("Error in Sample 2:", e)

try:
    result_sample_3 = concatenate_strings("-3", "%$")
    print("Sample 3 Result:", result_sample_3)
except Exception as e:
    print("Error in Sample 3:", e)

try:
    result_sample_4 = count_vowels("au#n6o..(0E")
    print("Sample 4 Result:", result_sample_4)
except Exception as e:
    print("Error in Sample 4:", e)