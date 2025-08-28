# Exception Handling

# Python provide 5 keyword to perform Exception Handling:

# 1. try
# 2. except
# 3. else
# 4. raise
# 5. finally

a = int(input("Enter first no:"))
b = int(input("Enter second no:"))
try:
    c = a/b
    print("Div is", c)
except ZeroDivisionError:
    print("Denominator should not be 0")
d = a+b
print("Sum is", d)
