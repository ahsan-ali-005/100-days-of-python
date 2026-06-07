# Validate email format

mail=input("Enter Your Email: ")

if mail.count("@")==1:
    parts=mail.split("@")
    username=parts[0]
    domain=parts[1]

    if domain!="" and username!="":
        
        if "." in domain and not domain.startswith(".") and not domain.endswith("."):
            print("The formate is correct!")
        else:
            print("Wrong Formate")
    else:
            print("Wrong Formate")

else:
            print("Wrong Formate")