class Number:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mul   (self):
        return self.num1*self.num2
    def div(self):
        assert(self.num2!=0),"number is divisible by 0"
        return self.num1/self.num2
n1=int(input())
n2=int(input())
ob=Number(n1,n2)
try:
    print(n1,'/',n2,'=',ob.div(),sep='')
except ZeroDivisionError as obj:
    print(obj)
print(n1,'-',n2,'=',ob.sub(),sep='')
print(n1,'*',n2,'=',ob.mul(),sep='')
print(n1,'+',n2,'=',ob.add(),sep='')
