def get_numbers(myList):
    mynumberList=[x for x in myList if type(x) is int]
    return mynumberList

myList=["bhopal",25,"$","hello",34,21,"indore",22]
print("Actual List")
print(myList)
print("List with numbers only")
mynumberList=get_numbers(myList)
print(mynumberList)