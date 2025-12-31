fin=None
fout=None
try:
    fin=open("e:/images/sachin.jpg",'rb')
    fout=open("e:/images/sachin2.jpg","wb")
    data=fin.read()
    fout.write(data)
    print("File copied successfully")
except(FileNotFoundError)as ex1:
    print("Could not open the file",ex1)
finally:
    if fin is not None:
        fin.close()
        print("File1 closed successfully")
    if fout is not None:
        fout.close()
        print("File2 closed successfully")