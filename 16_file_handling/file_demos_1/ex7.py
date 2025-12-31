f = None
try:
    f = open("data.txt", "w")
    text = input("Type a message:")
    upper = 0
    lower = 0
    digits = 0
    for ch in text:
        f.write(ch)
        if 65 <= ord(ch) <= 90:
            upper += 1
        elif 97 <= ord(ch) <= 122:
            lower += 1
        elif 48 <= ord(ch) <= 57:
            digits += 1
    print("File saved successfully")
    print("Total upper case letters:", upper)
    print("Total lower case letters:", lower)
    print("Total digits:", digits)
    print("Total special characters:", len(text) - (upper + lower + digits))
except FileNotFoundError as ex1:
    print("Can't create the file", ex1)
except OSError as ex2:
    print("Can't write the data in file", ex2)
finally:
    if f is not None:
        f.close
        print("File closed successfully!!")


# Type a message:Happy New Year , 2026
# File saved successfully
# Total upper case letters: 3
# Total lower case letters: 9
# Total digits: 4
# Total special characters: 5
# File closed successfully!!
