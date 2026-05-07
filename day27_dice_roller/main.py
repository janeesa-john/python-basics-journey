import random

count = 0
history = []
highest = 0

print("🎲 Welcome to Dice Roller")

while True:
    choice = input("\nRoll dice? (yes/no): ").lower()

    if choice in ["yes", "y"]:
        number = random.randint(1, 6)

        count += 1
        history.append(number)

        if number > highest:
            highest = number

        print("You got:", number)

    elif choice in ["no", "n"]:
        print("\nGoodbye!")
        print("Total Rolls:", count)

        if history:
            print("Roll History:", history)
            print("Highest Roll:", highest)

        break

    else:
        print("Invalid input. Please enter yes/no.")