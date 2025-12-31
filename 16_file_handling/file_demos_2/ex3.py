f=None
try:
    f=open("msg1.bin","wb")
    text=input("Type something:")
    data=text.encode()
    f.write(data)
except FileNotFoundError as e1:
    print("Cannot create the fie",e1)
except OSError as e2:
    print("Error while writing",e2)
finally:
    if f is not None:
        f.close()
        print("File closed successfully")