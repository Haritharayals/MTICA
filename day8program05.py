def div(a,b):
    assert( isinstance(a,int)or isinstance(a,float)),\
            'first Argumentbe either integer or float'
    assert( isinstance(b,int)or isinstance(b,float)),\
            'second Argumentbe either integer or float'
    assert (b!=0),"Division by zero is not defined"      
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
    print(Factorial('hello',20))
except Exception as obj:
    print(obj)

try:
    print(Factorial(20,'hello'))
except Exception as obj:
    print(obj)

     

     
