# Kon banega Crorepati

questions=[["What is the capital of Pakistan?", "Islamabad", "Lahore","Karachi","a"],["What is the National animal of Pakistan?","Markhor","Lion","Dog","a"],["What is the favourite color of me?","red","black","yellow","b"]]

levels=[1000,2000,5000,10000,100000,10000000]

i=0
n=0
for question in questions:
        print(f"For Rs.{levels[n]} answer the question correct.")
        print(question[i])
        print(f"a. {question[1]} b. {question[2]} \nc. {question[3]}")
        ans=input("Enter your answer (a-c): ")
        if ans == questions[i][-1]:
            print("Your Answer is Correct!")
            money=levels[n]
            print(f"You are taking home now: Rs.{money}")
            n+=1
            i+=1

        else:
            print("Your Answer is wrong!")
            money=0
            print(f"You lose prize. You are taking home: Rs.{money}")

