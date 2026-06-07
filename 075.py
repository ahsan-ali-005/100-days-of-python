# Monitor file changes (basic polling)

import os
import time

file="data.txt"

exists = os.path.exists(file)

if exists:
    last_modified = os.path.getmtime(file)

else:
    last_modified=None


while True:
    time.sleep(0.5)

    current_exists= os.path.exists(file)

    if not exists and current_exists:
        print("File Created!")

    elif exists and not current_exists:
        print("File Deleted!")

    elif current_exists:

        current_time=os.path.getmtime(file)

        if current_time!=last_modified:
            print("File Modified!")
            last_modified=current_time

    
    exists=current_exists