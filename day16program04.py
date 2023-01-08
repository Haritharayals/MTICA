def printresult(n):
    return[i[::-1] for i in n]

inp=input().strip().split()

print(*printresult(inp))
