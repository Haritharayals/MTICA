string='''practice problems for
list comprehension in python.'''

ans=[i for i in string if i not in'AEIOUaeiou']
print(*ans)
