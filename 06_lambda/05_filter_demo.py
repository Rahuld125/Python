def check_even(n):
    return n%2==0

mylist=[1,2,3,4,5,6]
result=filter(check_even,mylist)
print(type(result))
print(list(result))