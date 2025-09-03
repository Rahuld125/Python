def calculate(a, b):
    if a > 0 and b > 0:
        return a+b
    else:
        return "sum not possible"


ans = calculate(5, 10)
print(ans)
ans = calculate(5, -10)
print(ans)


# result=calculate(5,10)
# print(result)
# print(type(result))
