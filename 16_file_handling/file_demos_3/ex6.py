import os
import time

total_sec = os.path.getmtime("data.txt")
readable_time = time.ctime(total_sec)
print("File was last modified on", readable_time)
