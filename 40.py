# Create Student class and calculate avg marks

class Student:
    def __init__(self, name, marks_list):
        self.name = name
        self.marks_list = marks_list

    def average(self):
        total = 0
        for mark in self.marks_list:
            total += mark
        
        avg = total / len(self.marks_list)
        
        print(f"The average of the marks of {self.name} is {avg}.")

# --- Main Program ---
name = input("Enter your name: ")
n = int(input("Enter Number of Subjects: "))
marks_list = []

for i in range(1, n + 1):
    marks = int(input(f"Enter your {i} Subject Marks: "))
    marks_list.append(marks)

s1 = Student(name, marks_list)
s1.average()