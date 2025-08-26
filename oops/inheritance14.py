# If we want to call the parent class __init__(), then we have 2 options:

# 1. call it using the name of parent class explicitly
# 2. call it using the method super()


class A:
    def __init__(self):
        print("A's constructor called")


class B(A):
    def __init__(self):
        # Option 1
        # A.__init__(self)

        # Option 2
        super().__init__()
        print("B's constructor called")


obj = B()
