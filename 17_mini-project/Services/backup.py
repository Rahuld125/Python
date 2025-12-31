import pickle
from config import Config
import os


class Backup:
    def create_backup():
        if not os.path.exists(Config.STUDENT_FILE):
            print(f"Error: {Config.STUDENT_FILE} does not exist")
            return

        try:
            # Read the student records as text
            with open(Config.STUDENT_FILE, "r") as f:
                data = f.readlines()

            # Write the records in binary format using pickle
            with open(Config.BACKUP_FILE, "wb") as bf:
                pickle.dump(data, bf)

            print(f"Binary backup created successfully: {Config.BACKUP_FILE}")

        except Exception as e:
            print(f"Backup Error: {e}")
