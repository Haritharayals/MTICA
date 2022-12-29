num1=input("enter a number:")
num2=input("enter a number:")
try:
    res=int(num1)/int(num2)
except ZeroDivisionError:
    print("Exception handled by Haritha")
except ValueError:
    print("Exception handled by Prem")
except Exception as ob:
    print(ob)
else:
    print(num1,'/',num2,'=',res)
finally:
    print('Thanks')

print("visit again at python class at MTCA")
