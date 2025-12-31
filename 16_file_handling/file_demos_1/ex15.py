def read_nums_from_file(filename):
    f = None
    try:
        f = open(filename, "r")
        lines = f.readlines()
        if not lines:
            raise ValueError("Empty File")

        numbers = []
        for str in lines:
            str = str.strip()
            try:
                numbers.append(int(str))
            except ValueError:
                print(f"Skipping invalid value:{str}")

        if not numbers:
            raise ValueError("No valid numeric data found")

        print("Numbers read from file are")
        for n in numbers:
            print(n)
        total = sum(numbers)
        avg = total / len(numbers)
        print(f"Sum is {total}")
        print(f"Avg is {avg}")
    except ValueError as ex1:
        print("Error:", ex1)
    except FileNotFoundError as ex2:
        print("Error:", ex2)
    except OSError:
        print("Error in reading file")
    except Exception as ex3:
        print("Unexpected error", ex3)
    finally:
        if f is not None:
            f.close()
            print("File closed successfully")


read_nums_from_file("data1.txt")
