import os
import time
from config import Config


class FileUtils:
    def file_info():
        try:
            # Check if the file exists
            if not os.path.exists(Config.STUDENT_FILE):
                print("Student file does not exist.")
                return

            # Get the file size in bytes
            size = os.path.getsize(Config.STUDENT_FILE)

            # Get the last modified time(as a timestamp)
            modified_time = os.path.getmtime(Config.STUDENT_FILE)

            # Covert the timestamp to a human-readable format
            readable_time = time.ctime(modified_time)

            # Print the file info
            print(f"File: {Config.STUDENT_FILE}")
            print(f"Size: {size} bytes")
            print(f"Last Modified: {readable_time}")

        except Exception as e:
            print("File Info Error:", e)

    def rename_file():
        try:
            # Check if the original file exists
            if not os.path.exists(Config.STUDENT_FILE):
                print("Student file does not exist.")
                return

            # Enter new file name
            new_name = input("Enter new file name (with.txt): ").strip()
            if not new_name:
                print("File name cannot be empty.")
                return

            # Combine the directory path with the new file name
            new_path = os.path.join(Config.DATA_DIR, new_name)

            # Check if a file with the new name already exists
            if os.path.exists(new_path):
                print("A file with this name is already exists.")
                return

            # Rename the file
            os.rename(Config.STUDENT_FILE, new_path)

            # Update the global variable to reflect the new file name
            Config.STUDENT_FILE = new_path
            print("File renamed successfully.")

        except Exception as e:
            print("Rename Error:", e)

    def delete_backup_folder():
        try:
            # Check if the backup folder exists
            if not os.path.exists(Config.BACKUP_DIR):
                print("Backup folder does not exist.")
                return

            # Check if the folder is empty
            if os.listdir(Config.BACKUP_DIR):
                print("Backup folder is not empty.")
                return

            # Remove the empty backup folder
            os.rmdir(Config.BACKUP_DIR)
            print("Backup folder deleted successfully.")

        except Exception as e:
            print("Delete Backup folder Error:", e)
