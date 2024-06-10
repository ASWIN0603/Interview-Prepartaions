'''Let's learn about list comprehensions! You are given three integers (x,y,x)  and  representing the dimensions of a cuboid along with an 
integer n Print a list of all possible coordinates given by (i,j,k)  on a 3D grid where the sum of (i+j+k) is not equal to n. Here, 
Please use list comprehensions rather than multiple loops, as a learning exercise.'''


x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
cartesian_product = [[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]

print(cartesian_product)


