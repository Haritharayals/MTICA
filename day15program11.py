def outer():
    print('outer funcion')

    def inner():
        print('inner function')

    inner()

outer()
