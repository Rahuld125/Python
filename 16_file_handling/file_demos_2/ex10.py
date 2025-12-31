f = None
try:
    f = open("message1.txt", "x+")
    f.write("New file created")
    f.seek(0)
    str = f.read()
    print(str)
except FileNotFoundError:
    print("Cannot create the file")
except OSError:
    print("Cannot write/read in the file")
except Exception:
    print("Unexpected error")
finally:
    if f is not None:
        f.close()
        print("File closed successfully")
