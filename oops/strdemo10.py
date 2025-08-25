# Demonstration of the __str__ method: returns a string representation of an object.

# Key Points:
# 1. Since Python 3.0, every user-defined class automatically inherits from the base 'object' class.
#    (Explicitly: class Emp(object): or implicitly: class Emp:)

# 2. The 'object' class provides several special (magic) methods that all classes inherit.

# 3. Common special methods include:
#    - __init__(): Constructor, called when an object is created.
#    - __str__(): Returns a string representation of the object (used by print()).
#    - __new__(): Creates a new instance of the class.
#    - __del__(): Called when an object is about to be destroyed.


class Emp:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


e = Emp("Rahul", 25, 30000.0)
print(e)
