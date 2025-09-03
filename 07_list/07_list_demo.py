# def removevowels(txt):
#     myList=[]
#     for x in txt:
#         if x not in "aeiou":
#             myList.append(x)
#     return myList


def removevowels(txt):
    myList=[x for x in txt if x not in "aeiou"]
    return myList

text=input("Type a string:")
finalList=removevowels(text)
print(finalList)