'''Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and lambda functions
Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')'''


l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
q=map(lambda y:str(y),l)
print(tuple(q))