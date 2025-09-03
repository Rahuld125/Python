class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        feet = self.feet+other.feet
        inches = self.inches+other.inches
        if inches >= 12:
            feet = feet+inches//12
            inches = inches % 12
        d = Distance(feet, inches)
        return d

    def __str__(self):
        return f"feet={self.feet}, inches={self.inches}"


d1 = Distance(10, 6)
d2 = Distance(8, 9)
d3 = d1 + d2
print(d1)
print(d2)
print(d3)
