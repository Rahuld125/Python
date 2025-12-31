from setup import Setup
from Services.student import Student
from Services.backup import Backup
from Services.file_utils import FileUtils


class Main:
    def menu():
        while True:
            print("\n--- Student Record Management ---")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student by Roll No")
            print("4. Update Student Marks")
            print("5. Delete Student Record")
            print("6. Create Binary Backup")
            print("7. Show File Size & Last Modified Date")
            print("8. Rename Student File")
            print("9. Delete Backup Folder (if empty)")
            print("10. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                Student.add_student()
            elif choice == "2":
                Student.view_students()
            elif choice == "3":
                Student.search_student()
            elif choice == "4":
                Student.update_marks()
            elif choice == "5":
                Student.delete_student()
            elif choice == "6":
                Backup.create_backup()
            elif choice == "7":
                FileUtils.file_info()
            elif choice == "8":
                FileUtils.rename_file()
            elif choice == "9":
                FileUtils.delete_backup_folder()
            elif choice == "10":
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    Setup.setup()
    Main.menu()
