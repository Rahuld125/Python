mylist=[1,2,3,4,5,6]
result=filter(lambda n:n%2==0,mylist)
print(type(result))
print(list(result))