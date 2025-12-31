def increment_salaries(filename):
    f = None
    try:
        f = open(filename, "r+")
        lines = f.readlines()
        if not lines:
            raise ValueError("File is empty")
        updated_list = []
        for line in lines:
            line = line.strip()
            try:
                name, salary = line.split(",")
                salary = eval(salary)
                new_salary = salary * 1.25
                updated_list.append(f"{name},{new_salary}\n")
            except ValueError:
                print(f"Skipping {salary}")
        if not updated_list:
            raise ValueError("No valid records found")
        f.seek(0)
        f.writelines(updated_list)
        print("Salaries updated successfully")

    except ValueError as ex1:
        print("Error:", ex1)
    except FileNotFoundError as ex2:
        print("Cannot open the file", ex2)
    except OSError as ex3:
        print("Cannot update the file", ex3)
    except Exception as ex4:
        print("Unexpected error", ex4)
    finally:
        if f is not None:
            f.close()
            print("File closed successfully")


increment_salaries("emp.csv")
