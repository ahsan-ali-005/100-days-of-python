# Merge two files

with open("file1.txt") as f1:
    content1 = f1.read()

with open("file2.txt") as f2:
    content2 = f2.read()


with open("file3.txt" ,"w") as f:

    f.write(f"{content1}\n")
    f.write(content2)