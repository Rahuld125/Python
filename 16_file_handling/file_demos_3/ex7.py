import os
import time

obj = os.stat("data.txt")
print("File size is", obj.st_size, "bytes")
print("File was lat modified on", time.ctime(obj.st_mtime))
