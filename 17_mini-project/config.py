import os


class Config:
    # Define dir and file paths for student data and backup
    DATA_DIR = "data"
    BACKUP_DIR = "backup"

    STUDENT_FILE = os.path.join(DATA_DIR, "students.txt")
    BACKUP_FILE = os.path.join(BACKUP_DIR, "students_backup.bin")
