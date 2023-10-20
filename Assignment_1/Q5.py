'''Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3
[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]'''


d=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
h=filter(lambda x:(x%2==0 and x%3==0),d)
print('list that are divisible by 2 and 3 =',list(h))