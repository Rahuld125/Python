ch = input("Enter a character")

if "A" <= ch <= "Z":
    print("It is a capital letter")
elif "a" <= ch <= "z":
    print("It is a small letter")
elif "0" <= ch <= "9":
    print("It is a digit")
else:
    print("It is something else")
