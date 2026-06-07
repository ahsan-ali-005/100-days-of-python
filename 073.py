# Parse text and count paragraphs

with open("text.txt", "r") as f:
    data = f.read()

paragraphs = data.split("\n\n")
print(paragraphs)

count = 0
for p in paragraphs:
    if p.strip():
        count += 1

print("Total paragraphs:", count)