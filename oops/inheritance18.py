# How to check wheather a class is subclass of another class


class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(issubclass(B, A))  # True
print(issubclass(C, A))  # True
print(issubclass(A, B))  # False


# How to check wheather an object is instance of a class
a = A()
b = B()
c = C()
print(isinstance(a, A))  # True
print(isinstance(b, A))  # True
print(isinstance(c, A))  # True
print(isinstance(a, B))  # False
