'''Q4. Write a python program using reduce function to compute the product of a list containing numbers from 1 to 25.'''


from functools import reduce
o=[z for z in range(1,25)]
k=reduce(lambda x,y:x*y,o)
print("product of a list containing numbers from 1 to 25 =",k)
