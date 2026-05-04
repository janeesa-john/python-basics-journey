count = 0   # global variable


def increment():
    global count
    count += 1
    print("Count increased to:", count)


def decrement():
    global count
    count -= 1
    print("Count decreased to:", count)


def show():
    print("Current count:", count)


while True:
    print("\n🔢 Counter App")
    print("1. Increment")
    print("2. Decrement")
    print("3. Show Count")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        increment()
    elif choice == "2":
        decrement()
    elif choice == "3":
        show()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")