string=input()
##ans=[]
##for i in string:
##  if i 'AEIOUaeiou':
##    ans.append(i)
##print((*ans))

ans=[i for i in string if i in 'AEIOUaeiou']
print(*ans)
