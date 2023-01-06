def outer():
    message='outer funcion'
    print(message)

    def inner():
        print('inner function')

    inner()

outer()
