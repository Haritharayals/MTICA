"""string='''
practice problems for list com pre hension in python.
'''

wordsLst=string.split(' ')
print(wordsLst)
wordsLst=[i.strip("\n")for i in wordsLst]
print(wordsLst)
ans={i:i[::-1]for i in wordsLst}
print(ans)"""
ans=[]
for i in range(1,101):
    if i%2==0 or i%3==0 or i%4==0:
         ans.append(i)
print(*ans)
