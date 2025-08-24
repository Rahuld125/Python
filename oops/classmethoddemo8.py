# Class Method :

# 1. Class method is a method that is bound to the class and not the
#       object of the class.
# 2. To create a class method, we use the @classmethod "DECORATOR".

class Student:

    @classmethod
    def change_school(cls):
        cls.school = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, School: {self.school}")


Student.change_school()
print(Student.school)

s1 = Student("John", 20)
s1.display()
s2 = Student("Alice", 22)
s2.display()
