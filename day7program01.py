string='''
practice problems for list com pre hension in python.
'''

wordsLst=string.split(' ')
print(wordsLst)
wordsLst=[i.strip("\n")for i in wordsLst]
print(wordsLst)
#ans={word:len(word)for word in wordsLst}
ans={i:len(i)for i in wordsLst}
print(ans)
