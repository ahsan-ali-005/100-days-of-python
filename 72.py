# Game Hiscore Save in file Problem

import random

print("Your are Playing the Game!")

score=random.randint(0,10)

with open ("score.txt", "r") as f:

    hiscore= f.read()

    if hiscore == "":

        hiscore=0
    
    else:
        hiscore = int(hiscore)

print(f"Your Score is {score}")


if score>hiscore:
    print(f"New Hiscore: {score}")

    with open ("score.txt", "w") as f:

        f.write(str(score))