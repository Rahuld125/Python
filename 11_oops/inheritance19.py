# Multiple Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getname(self):
        return self.name

    def getage(self):
        return self.age


class Student:
    def __init__(self, roll, per):
        self.roll = roll
        self.per = per

    def getroll(self):
        return self.roll

    def getper(self):
        return self.per


class ScienceStudent(Person, Student):
    def __init__(self, name, age, roll, per, stream):
        Person.__init__(self, name, age)
        Student.__init__(self, roll, per)
        self.stream = stream

    def getstream(self):
        return self.stream


s = ScienceStudent("Alice", 20, 101, 88.5, "Physics")
print("Name:", s.getname())
print("Age:", s.getage())
print("Roll:", s.getroll())
print("Percentage:", s.getper())
print("Stream:", s.getstream())
