def get_upper(text):
    mylist=[x for x in text if x==x.upper() if x not in 'AEIOU']
    return mylist

text="I Live In Bhopal"
mylist=get_upper(text)
print(mylist)