def myfunc1():
    x="Jhan"
    def myfunc2():
        nonlocal x
        x="Hello"
    myfunc2()
    return x

print
