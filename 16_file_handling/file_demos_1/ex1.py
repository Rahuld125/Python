try:
    f = open("msg.txt", "w")
    f.write("Welcome To Python")
except FileNotFoundError as e1:
    print("Can't create the file:", e1)
except OSError as e2:
    print("Error while writing", e2)
f.close()
print("File saved successfully!!")
