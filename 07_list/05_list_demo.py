# a1b2c345de56

mynums=[]
text=input("Type an alphanumeric string:")
for ch in text:
    if ch in "0123456789":
        mynums.append(int(ch))

print("List is:",mynums)
print("Sum is:",sum(mynums))