#How do you handle exceptions in Python?

# by use try and except
try:
    result = 10 / 0  
except ZeroDivisionError:
    print("Error: Division by zero")