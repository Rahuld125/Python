class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        p = Point(x, y)
        return p

    def __str__(self):
        return f"x={self.x}, y={self.y}"


p1 = Point(10, 20)
p2 = Point(30, 40)
p3 = p1 + p2
print(p3)
p4 = p1 + p2 + p3
print(p4)
