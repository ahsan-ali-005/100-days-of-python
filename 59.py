# Copy content of one file to another

with open("new.txt", "r") as f:
    content =f.read()

with open("copy-new.txt", "w") as f:

    f.write(content)