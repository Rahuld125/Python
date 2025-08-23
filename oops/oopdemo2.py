import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def cal_area(self):
        area = math.pi * self.radius * self.radius
        print("Area:", area)

    def cal_circumference(self):
        circ = 2 * math.pi * self.radius
        print("Circumference:", circ)


r = int(input("Enter radius:"))
obj = Circle(r)
obj.cal_area()
obj.cal_circumference()