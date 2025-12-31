f = None
try:
    f = open("msg.txt", "x")
    f.write("Then I'll learn GEN AI")
except FileNotFoundError as e1:
    print("Cannot create the file", e1)
except OSError as e2:
    print("Error while writing", e2)
finally:
    if f is not None:
        f.close()
        print("File saved successfully")
