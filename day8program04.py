def div(a,b):
    assert(b!=0),"Division by zero is not defined"
    return a/b
try:
    print(div(55,0))
except AssertionError as obj:
    print(obj)
try:
    print(div(20,3))
except AssertionError as obj:
    print(obj)
try:
    print(Factorial(100,20))
except Exception as obj:
    print(obj)

     
