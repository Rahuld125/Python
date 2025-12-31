import os

for f in os.listdir():
    try:
        if os.path.isfile(f) and f.endswith(".txt"):
            os.remove(f)
            print(f"{f} removed")
        else:
            print(f"skipping {f}")
    except PermissionError as ex1:
        print(f"Could not delete {f} because {ex1}")
