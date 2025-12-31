try:
    with open("msg.txt", "a") as f:
        f.write("\nIts fun")
except FileNotFoundError as e1:
    print("Cannot create the file:", e1)
except OSError as e2:
    print("Error while writing", e2)
