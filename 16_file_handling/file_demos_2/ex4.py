f=None
try:
    f=open("msg1.bin","rb")
    data=f.read()
    print(data)
except FileNotFoundError as e1:
    print("Cannot create the fie",e1)
except OSError as e2:
    print("Error while reading",e2)
finally:
    if f is not None:
        f.close()
        print("File closed successfully")