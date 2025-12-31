import os
from config import Config


class Setup:
    def setup():
        try:
            # Create directories if it doesn't exist
            os.makedirs(Config.DATA_DIR, exist_ok=True)
            os.makedirs(Config.BACKUP_DIR, exist_ok=True)

            # Create student file if it doesn't exist
            if not os.path.exists(Config.STUDENT_FILE):
                open(Config.STUDENT_FILE, "w").close()

        except Exception as e:
            print("Setup Error:", e)
