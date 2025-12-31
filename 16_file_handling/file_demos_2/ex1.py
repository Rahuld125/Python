f=None
try:
    f=open("e:/images/sachin.jpg",'rb')
    data=f.read()
    print(type(data))
    print(data)
except(FileNotFoundError)as ex1:
    print("Could not open the file",ex1)
finally:
    if f is not None:
        f.close()
        print("File closed successfully")