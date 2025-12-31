f = None
lines = 0
try:
    f = open("message.txt", "w+")
    print("Type your text and to stop press ENTER")
    while True:
        str = input()
        if str == "":
            break
        f.write(str + "\n")
        lines += 1
    print(f"Total lines saved {lines}")
    print("Data saved in file")
    input("Press any key to read the file...")
    f.seek(0)
    lines = 0
    while True:
        str = f.readline()
        if str == "":
            break
        print(str.strip())
        lines += 1
    print(f"Total lines read {lines}")
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
