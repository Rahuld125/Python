import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)


class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return super().area() * self.height


c = Cylinder(5, 10)
print("Area of cylinder:", c.area())
print("Volume of cylinder:", c.volume())
print(Circle.area(c))
