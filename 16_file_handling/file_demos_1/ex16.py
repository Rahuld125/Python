def read_emp_file(filename):
    f = None
    try:
        f = open(filename, "r")
        lines = f.readlines()
        if not lines:
            raise ValueError("Empty File")
        employees = []
        salaries = []
        for rec in lines:
            try:
                rec = rec.strip()
                name, sal = rec.split(",")
                sal = eval(sal)
                employees.append((name, sal))
                salaries.append(sal)
            except ValueError:
                print(f"Skipping invalid sal {sal}")
        if not employees:
            raise ValueError("No valid employee data found")
        print("Employee Details")
        for e in employees:
            print(f"Name:{e[0]},Salary:{e[1]}")
        highest = max(salaries)
        lowest = min(salaries)
        avg = sum(salaries) / len(salaries)
        print(f"Highest salary:{highest}")
        print(f"Lowest salary:{lowest}")
        print(f"Average salary:{avg}")
    except ValueError as ex1:
        print("Error:", ex1)
    except FileNotFoundError as ex2:
        print("Error:", ex2)
    except OSError as ex3:
        print("Error in reading file", ex3)
    except Exception as ex4:
        print("Unexpected error", ex4)
    finally:
        if f is not None:
            f.close()
            print("File closed successfully")


read_emp_file("emp.csv")
