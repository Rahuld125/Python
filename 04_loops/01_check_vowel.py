str = input("Type a string")

i = 0
while i < len(str):
    ch = str[i]
    i = i + 1
    if ch in "aeiouAEIOU":
        print("{} contain vowels".format(str))
        break
else:
    print("{} doesn't contain any vowel".format(str))
