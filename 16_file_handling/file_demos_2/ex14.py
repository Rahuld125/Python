try:
    with open("msg.txt", "r") as f:
        for str in f:
            print(str, end="")
except FileNotFoundError as e1:
    print("Cannot read the file:", e1)
except OSError as e2:
    print("Error while writing", e2)
