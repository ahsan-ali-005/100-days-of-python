import os

for file in os.listdir():
    if file.endswith(".py"):
        num = file.replace(".py", "")
        if num.isdigit():
            new_name = f"{int(num):03d}.py"
            os.rename(file, new_name)
            print(f"{file} -> {new_name}")