# Create backup file system

import os

filename = input("Enter file name: ")

if not os.path.exists(filename):
    print("File does not exist!")
else:
    name, ext = os.path.splitext(filename)
    backup_name = name + "_backup" + ext

    count = 1

    while os.path.exists(backup_name):
        backup_name = f"{name}_backup{count}{ext}"
        count += 1

    with open(filename, "r") as original:
        data = original.read()

    with open(backup_name, "w") as backup:
        backup.write(data)

    print("Backup created:", backup_name)