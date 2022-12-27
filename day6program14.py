string='''practice problems for
list comprehension in python.'''
ans=[ch]
for i in string:
     if i not in'AEIOUaeiou':
          ans.append(i)
print(*ans)
