# Guess the number game with limited attempts

import random
num = random.randint(1,100)
attempt=5

while attempt>0:
    try:
        guess=int(input("Guess a Number(1-100): "))
    except Exception as e:
        print(e)
    else:
        if guess > num:
            print("Think of a lesser Number.")
            attempt-=1
            print(f"Attempts Remaining: {attempt}")
        elif guess < num:
            print("Think of a larger Number.")
            attempt-=1
            print(f"Attempts Remaining: {attempt}")
        else:
            print(f"Your Guess is Right {num}")
            break

if attempt==0:
    print(f"You lost! The Number was: {num}")