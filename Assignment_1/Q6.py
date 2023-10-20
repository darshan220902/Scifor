'''Q6. Write a python program to find palindromes in the given list of strings using lambda and filter function.
['python', 'php', 'aba', 'radar', 'level']'''

n=['python', 'php', 'aba', 'radar', 'level']
m=filter(lambda x:x==x[::-1],n )
print('list of strings which are palindrome',list(m))