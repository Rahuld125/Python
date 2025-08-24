# We can delete/remove instance variables in 2 ways:

# 1. Using the del class_name.class_variable_name from anywhere in 
#    the program.
# 2. Using the del cls.variable_name inside the class methods.

class Sample:
    i=10
    def __init__(self):
        del Sample.i  # Deleting class variable inside the class method
        # del self.i  # This will also work

print(Sample.__dict__)
s1=Sample()
print()
print(Sample.__dict__)