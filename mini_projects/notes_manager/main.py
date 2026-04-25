
def add_note():
    with open("notes.txt","a") as file:
        note = input("Enter notes: ")
        file.write(note + "\n")

def view_note():
    with open("notes.txt","r") as file:
        for line in file:
            print(line)

while True:
    print("\nNotes Manager")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter choice(1/2/3): ")

    if choice == '1':
        add_note()
        print("Note added successfully")

    elif choice == '2':
        view_note()

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid choice")