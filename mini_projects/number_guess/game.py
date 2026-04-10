# Number Guessing Game
# User has limited attempts to guess a randomly generated number

import random

rand = random.randint(1,100)
attempt = 0
while attempt < 6:
    number = int(input("Guess a number between 1 and 100: "))
    attempt+=1
    if rand == number:
        print(f"You guessed the correct number in {attempt} attempts!!!")
    elif rand < number:
        print("Too high")
    else:
        print("Too low")
else:
    print(f"Game Over! The correct number was {rand}")