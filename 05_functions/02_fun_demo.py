def absolute(n):
    if n < 0:
        n = -n
    return n


a = int(input("Enter the value:"))
x = absolute(a)
print("Abs of", a, "is", x)
