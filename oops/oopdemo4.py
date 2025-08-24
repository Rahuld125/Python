# There are 4 ways in python to create instance variables.

# 1. Using self keyword inside __init__()/constructor method.
# 2. Using self keyword inside any other method.
# 3. Using object reference outside the class.
# 4. Using __dict__ attribute of the object.


# We can delete/remove instance variables in 2 ways.

# 1. Using del self.<var_name> from the body of any instance method within the class
# 2. Using del <obj_ref>.<var_name> from outside the class

class Boy:
    def __init__(self, name, girlfriend):
        self.name = name
        self.girlfriend = girlfriend

    def breakup(self):
        del self.girlfriend


b1 = Boy("Deepak", "Jyoti")
print(b1.__dict__)
b1.breakup()
print(b1.girlfriend)
