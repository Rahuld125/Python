mynums=[]
for i in range(1,6):
    x=int(input("Enter "+str(i)+" element"))
    mynums.append(x)
print("The list is")
total=0
for i in mynums:
    print(i)
    total+=i
print("Sum of nos is", total)