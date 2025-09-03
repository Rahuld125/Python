# Static method : A method which does not take self or cls as the first argument


#   If we do not use the decorator @staticmethod, then 2 things can happen:

#   1. If we call the method using the object reference, Python will consider it to
#      be an instance method
#   2. If we are calling it using the classname, then Python will consider it to be a
#      static method


class MyMath:
    @staticmethod
    def add(x, y):
        return x + y


result = MyMath.add(5, 3)
print("The sum is:", result)
