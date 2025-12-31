f=None
try:
    f=open("msg.txt","r+")
    text=f.read()
    print(text)
    f.seek(0)
    f.write("Hello")
    f.write("From")
    f.seek(0)
    print("After changing")
    text=f.read()
    print(text)
except FileNotFoundError as e1:
    print("Cannot create or open the file",e1)
except OSError as e2:
    print("Cannot create write or read the file",e2)
finally:
    if f is not None:
       f.close()
       print("File closed")