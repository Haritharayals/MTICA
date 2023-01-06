def findFactor(n):
    temp=list()
    for i in range(1,n+1):
        if n%1==0:
            temp.append(i)
    return temp
a=int(input())
print(*findFactor(a))
