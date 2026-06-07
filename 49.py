# Create To-Do list class

class To_Do_list:

    def __init__(self):
        self.dic = {}  
        self.counter = 1

    def add_task(self):
        task_name = input("Enter Task Name: ")
        self.dic[self.counter] = {"task": task_name, "done": "Pending"}
        print("Task Added Successfully!")
        self.counter += 1

    def remove_task(self):
        task_name = input("Enter Task Name to remove: ")
        to_delete = None

    
        for key, value in self.dic.items():
            if value["task"] == task_name:
                to_delete = key
                break

        if to_delete:
            del self.dic[to_delete]
            print(f"Task '{task_name}' removed successfully!")
        else:
            print(f"No Task Found with name '{task_name}'")

    def mark_complete(self):
        task_name = input("Enter Task Name to mark complete: ")
        to_delete = None

  
        for key, value in self.dic.items():
            if value["task"] == task_name:
                to_delete = key
                break

        if to_delete:
            del self.dic[to_delete]  # auto-remove on completion
            print(f"Task '{task_name}' marked complete and removed!")
        else:
            print(f"No Task Found with name '{task_name}'")

    def view_tasks(self):
        if not self.dic:
            print("No Task So far!")
        else:
            for key, value in self.dic.items():
                print(f"{value['task']} = {value['done']}")


t = To_Do_list()

while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task Complete (Auto Remove)")
    print("4. View Tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        t.add_task()
    elif choice == "2":
        t.remove_task()
    elif choice == "3":
        t.mark_complete()
    elif choice == "4":
        t.view_tasks()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice!")