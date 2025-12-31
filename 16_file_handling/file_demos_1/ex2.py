a = 10
b = 20


def show():
    x = 5
    y = 7
    print("Inside show...")
    print(locals())


show()
print(globals())
