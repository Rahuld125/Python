# 1. Every object in python has an attribute denoted by __dict__.
# 2. This attribute is automatically added by python and it contains all the
#    attributes defined for the object itself.
# 3. It maps the attribute names to their corresponding values.


# There are 4 ways in python to create instance variables.

# 1. Using self keyword inside __init__()/constructor method.
# 2. Using self keyword inside any other method.
# 3. Using object reference outside the class.
# 4. Using __dict__ attribute of the object.

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


e = Employee("John", 25, 50000)
print(e.__dict__)  # {'name': 'John', 'age': 25, 'salary': 50000}

e.__dict__['age'] = 26
print(e.__dict__)  # {'name': 'John', 'age': 26, 'salary': 50000}

e.__dict__['department'] = 'IT'
# {'name': 'John', 'age': 26, 'salary': 50000, 'department': 'IT'}
print(e.__dict__)
