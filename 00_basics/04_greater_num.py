a, b, c = input("Enter 3 int").split()
a = int(a)
b = int(b)
c = int(c)

# list comprehension problem

if a > b:
    if a > c:
        print("Gr no is {}".format(a))
    else:
        print("Gr no is {}".format(c))
else:
    if b > c:
        print("Gr no is {}".format(b))
    else:
        print("Gr no is {}".format(c))
