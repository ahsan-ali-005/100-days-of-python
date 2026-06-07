# Extract emails from text file

domains=["@gmail.com","hotmail.com","@yahoo.com"]

with open("emailsfile.txt","r") as f:

    for line in f:

        words = line.split()

        for word in words:

            word = word.strip(",.?!")
            if "@" in word and any(word.endswith(domain) for domain in domains):

                if word.split("@")[0] != "":
                    print(f"Email: {word}")

