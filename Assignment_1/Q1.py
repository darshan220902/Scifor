## Q1. Create a python program to sort the given list of tuples based on integer value using lambda function.[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]


f=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
j=sorted(f,key = lambda x : x[1],reverse=True) # sort by descending
s=sorted(f,key = lambda x : x[1]) # sort by ascending
print('sort by descending',list(j))

print('sort by ascending',list(s))