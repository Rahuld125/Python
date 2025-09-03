import traceback

while (True):
    try:
        a = int(input("Input first no:"))
        b = int(input("Input second no:"))
        c = a/b
        print("Div is ", c)
        break
    except:
        print(traceback.format_exc())
