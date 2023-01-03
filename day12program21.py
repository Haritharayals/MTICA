class Number:
    def __init__(self,n):
        self.n=n
    def calculateFactorial(self):
        if self.n==0:
            return "even"
        res=1
        for i in range(1,self.n+1):
            res*=i
        return res
    def checkEvenOdd(self):
         if self.n%2==0:
            return "Even"
         else:
            return "odd"
    def SumOfDigits(self):
        if self.n<0:
            self.n=abs(self.n)
        temp=str(self.n)
        t=0
        for i in temp:
            t+=int(i)
        return t
inp=int(input())
obj=Number(inp)
print('Factorial of',inp,obj.calculateFactorial())
print(inp,'is',obj.checkEvenOdd())
print('Sum Of Digits of',inp,'is',obj.SumOfDigits())


