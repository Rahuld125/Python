while (True):
    try:
        a = int(input("Input first no:"))
        b = int(input("Input second no:"))
        if a <= 0 or b < 0:
            raise Exception("Negative numbers not allowed!Try again")
        c = a/b
        print("Div is ", c)
        break
    except ValueError:
        print("Please input integers only! Try again")
    except ZeroDivisionError:
        print("Please input non-zero denominator")
    except Exception as e:
        print(e)
