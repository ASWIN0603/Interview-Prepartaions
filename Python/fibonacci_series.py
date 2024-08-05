# n = 10
# for i in range(0,n+1):
#     if i == 0:
#         num = 0
#         prev_2 =0
#     elif i == 1:
#         num = 1
#         prev_1=1
#     else:
#        num = prev_1 + prev_2
#        prev_2 = prev_1
#        prev_1 = num
       
#     print(num)
    

def fibonacci(n):
    if n < 0 :
        return 0
    elif n == 0:
        return 1
    else:
        fib = [0] * (n +1)
        fib[1] = 1
        for i in range(2,n+1):
            fib[i]=fib[i-1] + fib[i-2]
        return fib
    
print(fibonacci(10))
        
    