try:
    with open("msg.txt", "w") as f:
        f.write("I am learning File Handling")
except FileNotFoundError as e1:
    print("Cannot create the file:", e1)
except OSError as e2:
    print("Error while writing", e2)
