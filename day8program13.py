def checkEven(num1):
    if num1%2==0:
         return "even"

        
def checkOdd(num1):
    if num1%2==0:
         return "Odd"


num=int(input("enter a no:"))
x=checkEven(num)
y=checkOdd(num)


print("x=",x)
print("y=",y)

print(checkEven(num))
print(checkOdd(num))                   
