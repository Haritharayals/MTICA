def checkEven(num1):
    if num1%2==0:
         return "Even"

def checkOdd(num1):
    if num1%2==1:
         return "Odd"


num=int(input("enter a no:"))
print(checkEven(num))
print(checkOdd(num))                   

