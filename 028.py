# Create simple quiz game

print("======Quiz Time======")

d={
    """What is the capital of Pakistan?
    a) Lahore
    b) Islamabad
    c) Karachi""" : "b",
    """What is the national animal of Pakistan?
    a) Markhor
    b) Lion
    c) Bull""" : "a",
    """What is the national bird of Pakistan?
    a) Chakor
    b) Sparrow
    c) Parrot""" : "a",
    """What is the national flower of Pakistan?
    a) Jasmine
    b) Rose
    c) Lilly""" : "a",
    """What is the national sports of Pakistan?
    a) Cricket
    b) Football
    c) Hockey""" : "c"

}

score=0

for question in d:
    print(question)
   
    ans=input("Enter Your Answer(a/b/c): ").lower()

    if ans==d[question]:
        print("Correct!")
        score+=1
    else:
        print("Wrong!")


print(f"Your score is {score}/5")






    