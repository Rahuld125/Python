text = input("Enter a string")
i = 0

while i < len(text):
    ch = text[i]
    i += 1
    if ch in "aeiouAEIOU":
        continue
    print(ch)
