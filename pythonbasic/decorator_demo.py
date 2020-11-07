# python decorator demo


# functions
def add_one(number):
    return number + 1


print(add_one(1))


def say_hello(name):
    print("hello " + name)


say_hello("John")


# use function as a parameter
def greet_bob(say_hello_func):
    return say_hello_func("Bob")


# call the function which use function as a parameter
greet_bob(say_hello)


# inner function
def parent():
    print("hello from parent")

    def first_child():
        print("hello from first child")

    def second_child():
        print("hello from second child")

    first_child()
    second_child()


parent()


# smarter parent can choose different child according the input
def smarter_parent(num):
    def first_child():
        print("hello from first child of smarter parent")

    def second_child():
        print("hello from second child of smarter parent")

    if num == 1:
        return first_child()
    else:
        return second_child()


smarter_parent(1)

smarter_parent(2)


# simple decorator without parameters
def simple_decorator(func):
    def wrapper():
        print("something done before the func")
        func()
        print("something done after the func")

    # notice: there is not parenthesis after function name wrapper
    return wrapper


# use decorator just like a function calling
def hola():
    print("hola, decorator")


hola()

simple_decorator(hola)


# handsome decorator format
@simple_decorator
def handsome_hola():
    print("handsome decorator help you with less code")


handsome_hola()


# another decorator example is always good
def do_twice_decorator(func):
    def wrapper_do_twice():
        func()
        func()

    return wrapper_do_twice


@do_twice_decorator
def say_something_important():
    print("this is a very important notice!")


say_something_important()


# decorator with parameters
def do_three_times(func):
    def wrapper_do_three_times(*args, **kwargs):
        print("It must be very important!")
        func(*args, **kwargs)
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_three_times

# use the handsome format
@do_three_times
def very_important_notice(name):
    print(name + " has said something you must hear")

very_important_notice("John")

# use decorator as functions call
parent = do_three_times(parent)

parent()