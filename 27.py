# Create number guessing game

import random

a =random.randint(1,100)

attempts=0

while True:

    try:


        num=int(input("Guess a Number b/w 1-100: "))
        attempts+=1


        if num == a:
            print(f"You have Guessed Right: {a}")
            print(f"Your attempts are : {attempts}")
            break

        elif num > a:
            print("Think for a Small Number.")

        elif num < a:
            print("Think for a Large Number.")
        
        

        print(f"Your attempts are : {attempts}")

    except ValueError as e:
        print(e)