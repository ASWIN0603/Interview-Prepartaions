#convert roman numbers to decimal numbers 


#get a roman number as string
romannumber  = input("enter a sting")
list = []
final = 0
#Assign values for every letters in the string
for letter in romannumber:       
    if letter  == 'I':
        list.append(1)  
    elif letter == 'V':
        list.append(5)
    elif letter == 'X':
        list.append(10)
    elif letter == 'C':
        list.append(100)
    elif letter == 'M':
        list.append(1000)
print(list)
#if a number is lesser than the next element then it should be taken as negative
for i in range(len(list)):
    if i < len(list) - 1 and list[i] < list[i+1]:
        final -= list[i]
    else:
        final += list[i]

   
print(final)
    
        

