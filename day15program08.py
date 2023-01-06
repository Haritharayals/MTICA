def outer():
    message = 'outer scope'
    print(message)

    def inner():
        nonlocal message
        message = 'inner scope'
        print(message)

    inner()

    print(message)


outer()
