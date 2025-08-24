# In Python, a class can have 3 types of variables:

#  1. Instance Variable : Created per instance basis
#  2. Local Variables : Created locally inside a method and destroy when
#                       the method execution is over.
#  3. Class Variables :


class Emp:
    def __init__(self, name, age, salary):
        # instance variables
        self.name = name
        self.age = age
        self.salary = salary

    # instance method
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")


e = Emp("Rahul", 25, 30000.0)
f = Emp("Sonam", 24, 35000.0)
e.show()
f.show()
