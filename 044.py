# Create Logger class (writes to file)

class logger:

    def __init__(self,file_name):
        self.file_name=file_name

    def log(self,message):
        
        with open(self.file_name, "a") as f:
            f.write(message + "\n")
            print("Message Logged!")



l1 = logger("file.txt")

while True:
    msg=input("Enter log (type 'exit' to stop):") 

    if msg.lower() == "exit":
        break

    l1.log(msg)