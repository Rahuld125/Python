# demonstration of destructor in Python

# __del__ method is called when an object is about to be destroyed

class Test:
    def __init__(self):
        print("Object is created")

    def __del__(self):
        print("Object is destroyed")


def fun():
    t = Test()
    del t
    print("Inside fun()")


fun()
print("Have a good day!")
