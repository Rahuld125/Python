# MRO : Method Resolution Order
# The order in which base classes are searched when executing a method.


class A:
    def m(self):
        print("m of A called")


class B:
    def m(self):
        print("m of B called")


class C(A, B):
    pass


obj = C()
obj.m()

print(C.mro())  # [C, A, B, object]
print(C.__mro__)  # (C, A, B, object)
