# We can delete/remove instance variables in 2 ways.

# 1. Using del self.<var_name> from the body of any instance method within the class
# 2. Using del <obj_ref>.<var_name> from outside the class


class Engineer:
    def __init__(self, girlfried, job):
        self.girlfriend = girlfried
        self.job = job

    def fired(self):
        del self.job


e1 = Engineer("Anjali", "SDE")
print(e1.__dict__)
e1.fired()
del e1.girlfriend
print(e1.__dict__)


# class Boy:
#     def __init__(self, name, girlfriend):
#         self.name = name
#         self.girlfriend = girlfriend

#     def breakup(self):
#         del self.girlfriend


# b1 = Boy("Deepak", "Jyoti")
# print(b1.__dict__)
# b1.breakup()
# print(b1.girlfriend)
