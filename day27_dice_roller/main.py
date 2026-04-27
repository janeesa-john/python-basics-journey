import random

print("🎲 Dice Roller")

while True:
    choice = input("Roll dice? (yes/no): ").lower()

    if choice == "yes":
        number = random.randint(1, 6)
        print("You got:", number)

    elif choice == "no":
        print("Goodbye!")
        break

    else:
        print("Invalid input. Please enter yes or no.")