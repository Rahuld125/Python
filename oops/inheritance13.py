# super() : Accessing parent class methods

# Using super() is required in 2 situations:

# 1. For calling parent class constructor
# 2. For calling overridden methods

class A:
    def __init__(self):
        print("A's constructor called")


class B(A):
    def __init__(self):
        print("B's constructor called")


obj = B()


# 1. In the above code, A's constructor is not called when we create
#    an object of class B.

# 2. To call A's constructor, we can use super() in B's constructor
#    as shown below:
