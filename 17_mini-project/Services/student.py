from config import Config


class Student:
    def add_student():
        try:
            roll = input("Enter Roll No: ").strip()
            name = input("Enter Name: ").strip()
            marks = input("Enter Marks: ").strip()

            # Stop if any field is empty
            if not roll or not name or not marks:
                print("Fields cannot be empty.")
                return

            # Check for duplicate roll number
            with open(Config.STUDENT_FILE, "r") as f:
                for record in f:
                    existing_roll = record.strip().split(",")[0]
                    if existing_roll == roll:
                        print(f"Roll No {roll} already exists. Cannot add duplicate.")
                        return

            # If no duplicate, add student
            with open(Config.STUDENT_FILE, "a") as f:
                f.write(f"\n{roll},{name},{marks}\n")
            print("Student added successfully.")

        except Exception as e:
            print("Add Student Error:", e)

    def view_students():
        try:
            # Open the student file and read all lines
            with open(Config.STUDENT_FILE, "r") as f:
                records = f.readlines()

            # Check if the file is empty
            if not records:
                print("No records found.")
                return

            # Display the records
            for record in records:
                roll, name, marks = record.strip().split(",")
                print(f"Roll No: {roll}, Name: {name}, Marks: {marks}")

        except FileNotFoundError:
            print("Student not found")
        except ValueError:
            print("File format error")
        except Exception as e:
            print("View Error:", e)

    def search_student():
        try:
            # Enter the roll number
            roll_search = input("Enter Roll No to search: ").strip()
            found = False

            # Check if input is empty
            if not roll_search:
                print("Roll number cannot be empty")

            # Print the details of Student
            with open(Config.STUDENT_FILE, "r") as f:
                for record in f:
                    roll, name, marks = record.strip().split(",")
                    if roll == roll_search:
                        print(f"Found -> Roll No: {roll}, Name: {name}, Marks: {marks}")
                        found = True
                        break

            # If student not found
            if not found:
                print("Student not found.")

        except FileNotFoundError:
            print("Student file not found")
        except Exception as e:
            print("Search Error:", e)

    def update_marks():
        try:
            # Enter the roll number and new marks from the user
            roll_update = input("Enter Roll No to update marks: ").strip()
            new_marks = input("Enter new marks").strip()

            updated = False
            records = []

            # Open the student file and read all records
            with open(Config.STUDENT_FILE, "r") as f:
                for record in f:
                    roll, name, marks = record.strip().split(",")
                    if roll == roll_update:
                        records.append(f"{roll},{name},{new_marks}\n")
                        updated = True
                    else:
                        records.append(record)

            # Write all records back to the file
            with open(Config.STUDENT_FILE, "w") as f:
                f.writelines(records)

            # Inform the user whether the update was successful or not
            print("Marks updated." if updated else "Student not found.")

        except FileNotFoundError:
            print("Student file not found")
        except Exception as e:
            print("Update Error:", e)

    def delete_student():
        try:
            # Enter the roll no
            roll_delete = input("Enter Roll No to delete: ").strip()
            records = []
            deleted = False

            # Read all student records
            with open(Config.STUDENT_FILE, "r") as f:
                for record in f:
                    parts = record.strip().split(",")
                    if len(parts) != 3:
                        print(f"Skipping malformed record: {record.strip()}")
                        continue
                    roll, name, marks = parts
                    if roll == roll_delete:
                        deleted = True
                    else:
                        records.append(record)

            # Write back the remaining records to file
            with open(Config.STUDENT_FILE, "w") as f:
                f.writelines(records)

            print("Record deleted" if deleted else "Student not found")

        except FileNotFoundError:
            print("Student file not found")
        except Exception as e:
            print("Delete Error:", e)
