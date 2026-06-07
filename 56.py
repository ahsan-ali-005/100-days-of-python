# Replace word in file

with open("new.txt" , "r") as f:

    content = f.read()

content=content.replace("ahsan", "Larry")

with open("new.txt","w") as f:
    f.write(content)
