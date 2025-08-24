# Obtaining Details of Class Variables
# 1. class variables are owned by the class itself, so to store their details a
#    class also uses a dictionary named __dict__.

# 2. Thus we can see that Python has 2 dictionaries called __dict__.

# 3. One is <class-name>.__dict__ and the other is <object-ref>.__dict__.

class Emp:
    raise_per = 7.5  # class variable
    comp_name = "XYZ Pvt Ltd"  # class variable

    def __init__(self, age, name, sal):
        self.age = age  # instance variable
        self.name = name  # instance variable
        self.sal = sal  # instance variable


e1 = Emp(23, "Alice", 45000)
print(e1.__dict__)  # instance variable details
print()
print(Emp.__dict__)  # class variable details
