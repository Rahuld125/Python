name=input("Enter name")
vowels=list(filter(lambda ch : ch.lower() in "aeiou",name))
if len(vowels)==0:
    print("No vowels")
else:
    print(vowels)