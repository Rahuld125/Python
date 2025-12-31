f=None
try:
    f=open("msg.txt","a+")
    f.seek(0)
    text=f.read()
    print("File data:",text)
    f.seek(-10,2)# will throw exception
except FileNotFoundError as e1:
    print("Cannot create or open the file",e1)
except OSError as e2:
    print("Cannot create write or read the file",e2)
finally:
    if f is not None:
       f.close()
       print("File closed")