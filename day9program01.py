def printseriesDecresing(ch,n):
    assert isinstance(ch,str),"first argument should be string"
    assert isinstance(ch,int),"second argument should be int"
    for i in range(n,0,1):
        print(ch*i)
    return None



inpch=input("enter  a charcter:")
inpNum=int(input("enter ano:"))
print('-'*40)
try:
   printSeriesIncresing(inpch,inpNum)
except AssertionError as ob:
    print(ob)
  

