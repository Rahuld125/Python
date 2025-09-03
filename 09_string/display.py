name = "Rahul"
age = 25

# old way
# print("My name is "+name+" and my age is "+str(age))
# print("My name is", name, "and my age is", age)
# print("My name is {} and my age is {}".format(name, age))
# print("My name is %s and my age is %d" % (name, age))

# new way
print(f"My name is {name} and my age is {age}")

a = 10
b = 20
print(f"Their sum is {a+b}")
print(f"Greater num is {max(a, b)}")

# Vowels counting
vowels = ["a", "e", "i", "o", "u", "a"]
ch = "a"
print(f"{ch} in occurring in {vowels} = {vowels.count(ch)} times")

name = "guido van rossum"
newname = name.capitalize()
print(f"Original name is {name}\nCapitalized name is {newname}")

name = "Rahul Dharpure"
lc = name.lower()
uc = name.upper()
print(f"Original name is {name}")
print(f"Lower name is {lc}")
print(f"Upper name is {uc}")

newname = name.swapcase()
print(f"Swapped name is {newname}")

text = "we got independence in 1947"
newtext = text.title()
print(f"Original text is {text}")
print(f"Title text is {newtext}")

text = "i lOVe pYTHoN"
print(text.title())

text = "physics,chemistry,maths"
print(text.title())

text = "He's an engineer, isn't he?"
print(text.title())

s="this is good"
print(s.islower())

s="thi!s is a1so g00d"
print(s.islower())

s="this is Not good"
print(s.islower())