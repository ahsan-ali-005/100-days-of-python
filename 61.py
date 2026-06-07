# Create CSV reader and analyzer

import csv

count=0
total_marks=0

with open("data.csv", "r") as f:

    reader = csv.reader(f)  
    next(reader)  # skip header

    for row in reader:
        marks=int(row[2])
        total_marks+=marks
        count+=1


average=total_marks/count

print(f"Total Marks are: {total_marks}")
print(f"Total Students are: {count}")
print(f"Average of Marks are: {average}")