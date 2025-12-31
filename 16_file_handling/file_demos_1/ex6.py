f = None
try:
    f = open("msg.txt", "w")
    f.write("I am learning File Handling")
except FileNotFoundError as e1:
    print("Cannot create the file", e1)
except OSError as e2:
    print("Cannot write the data", e2)
finally:
    if "f" in locals():
        f.close()
        print("File saved successfully")
