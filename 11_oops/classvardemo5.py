# Class variable :

# 1. Class variable are those variables which are defined within
#    the class body outside any method.
# 2. They are also called as static variables, although there is
#    no static keyword used with them.
# 3. They are shared by all the instances of the class and have
#    the same value for each instance of the class.
# 4. They have a single copy in maintained at the "class level".


# Class Level : 
# 1. Class level is the memory area where class variables are stored.


# We can use class variables at 6 places :

# 1. Inside the class body but outside any method.
# 2. Inside the constructor using class name or using self.
# 3. Inside instance methods using class name or using self.
# 4. Inside class methods using class name or using special reference cls.
# 5. Inside static methods using class name only.
# 6. Outside the class using class name only.
# Note : We can not use class variables inside instance methods,


# How to access and modify class variables :

# The class variables can be accessed in 4 ways :
# 1. Using class name.
# 2. Using self (inside instance methods and constructor).
# 3. Using cls (inside class methods).
# 4. Using object reference (but not recommended).


class Emp:
    # 1. class variable
    # raise_amount = 7.5

    def __init__(self, age, name, sal):
        # 2. class variable : using class name
        # Emp.raise_amount = 7.5
        self.age = age
        self.name = name
        self.sal = sal

    def set_raise_amount(self):
        # 3. class variable : using class name
        Emp.raise_amount = 7.5

    def increase_sal(self):
        self.sal = self.sal + (self.sal * Emp.raise_amount / 100)

    def display(self):
        print(f"Name : {self.name}, Age : {self.age}, Salary : {self.sal}")


e1 = Emp(23, "Alice", 45000)
e1.set_raise_amount()
e2 = Emp(25, "Bob", 55000)
print("Before Salary Increment : ")
e1.display()
e2.display()
e1.increase_sal()
e2.increase_sal()
print("After Salary Increment : ")
e1.display()
e2.display()
print(f"Salary incremented by {Emp.raise_amount} %")
