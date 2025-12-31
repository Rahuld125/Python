f=None
try:
    f=open("msg.txt","w+")
    print("Initial content")
    text=f.read()
    print(text)
    f.write("Gen AI\n")
    f.write("is an essesntial skill today")
    print("After changing")
    f.seek(0)
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