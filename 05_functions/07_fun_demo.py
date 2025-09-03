def findlargest(*a):
    max = 0
    largest = ""
    for s in a:
        if len(s) > max:
            max = len(s)
            largest = s
    return max, largest


result = findlargest("January", "April", "September", "July")
print(result)
