import math


# Types of methods
# 1. Instance method : called using object reference
# 2. Class method : called using class name
# 3. Static method : called using class name

# Instance method : 

# 1. These are called instance methods because they can access instance members of the object.
# 2. The first argument is always self which refers to the current object.
# 3. We can access instance variables and instance methods using self keyword.

class Circle:
    # constructor
    def __init__(self, radius):
        self.radius = radius
    # instance method

    def cal_area(self):
        area = math.pi * self.radius * self.radius
        print("Area:", area)
    # instance method

    def cal_circumference(self):
        circ = 2 * math.pi * self.radius
        print("Circumference:", circ)


r = int(input("Enter radius:"))
obj = Circle(r)
obj.cal_area()
obj.cal_circumference()
