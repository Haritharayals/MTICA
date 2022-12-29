##def kelvinToFahrenheit(Temparature):
##    assert (Temparature>=0),"colder than absolute zero at MTICA!"
##    res=((Temparature-273)*1.8)+32
##    return res
##try:
##     print(kelvinToFahrenheit(-50))
##except Exception as ob:
##     print (ob)
##try:
##     print(KelvinToFahrenheit(273))
##except Exception as ob:
##     print (ob)
##try:
##     print(KelvinToFahrenheit(505.78))
##except Exception as ob:
##     print (ob)
##try:
##     print(KelvinToFahrenheit(-5))
##except Exception as ob:
##     print (ob)
##print("Thank you")



def Factorial(num):
    assert(isinstance(num,int)),"Factorial not defined for not integer"
    assert(num>=0),"Factorial of negative number is not defined!"
    if num==0:
        return 1
    else:
        return num*Factorial(num-1)

try:
    print(Factorial(-45))
except Exception as obj:
    print(obj)
try:
    print(Factorial(4.9))
except Exception as obj:
    print(obj)
try:
    print(Factorial(45))
except Exception as obj:
    print(obj)
try:
    print(Factorial('today'))
except Exception as obj:
    print(obj)

        
