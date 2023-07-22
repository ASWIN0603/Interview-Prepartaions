#GCD of two numbers 

def gcd(number_1, number_2):
    if number_2 == 0:
        return number_1
    else:
        return gcd(number_2, number_1 % number_2)

number_1 = int(input('Enter number 1: '))
number_2 = int(input('Enter number 2: '))

result = gcd(number_1, number_2)
print('GCD:', result)
