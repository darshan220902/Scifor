# How can you iterate through a list in Python?

# by for loop
l = [1, 2, 3, 4, 5]
for item in l:
    print(item)

# by while loop
l=[1,2,3,4]
i=0
while len(l)>i:
    print(l[i])
    i+=1

# by list compheresion
l = [1, 2, 3, 4, 5]
squared_list = [item ** 2 for item in l]
print(squared_list)
