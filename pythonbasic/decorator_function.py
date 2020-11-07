# decorator demo with function only

def simple_decorator(func):
    def wrapper():
        func()
        func()

    return wrapper


def what_up():
    print("what")


what_up = simple_decorator(what_up)

what_up()