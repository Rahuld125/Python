while (True):
    try:
        a = int(input("Input first no:"))
        b = int(input("Input second no:"))
        c = a/b
        print("Div is", c)
        break
    except ValueError:
        print("Please input integers only! Try again")
    except ZeroDivisionError:
        print("Please input non-zero denominator")
