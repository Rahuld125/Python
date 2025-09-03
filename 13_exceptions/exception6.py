import sys


try:
    a = int(input("Enter first no:"))
    b = int(input("Enter second no:"))
    c = a / b
    print("Div is ", c)
    # break
    sys.exit(0)
except ZeroDivisionError:
    print("Denominator must not be 0")
finally:
    print("Have a good day!")
