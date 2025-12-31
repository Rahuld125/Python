try:
    with open("msg.txt", "r") as f1, open("msg2.txt", "w") as f2:
        f2.write(f1.read())
except FileNotFoundError as e1:
    print("Cannot read the file:", e1)
except OSError as e2:
    print("Error while writing", e2)
