
def add_note():
    with open("notes.txt","a") as file:
        note = input("Enter notes: ")
        file.write(note + "\n")
    print("Note added successfully")

def view_note():
    with open("notes.txt","r") as file:
        for line in file:
            print(line)

def search_note():
    keyword = input("Enter keyword to search: ").lower()

    with open("notes.txt", "r") as file:
        found = False

        for line in file:
            if keyword in line.lower():
                print(line.strip())
                found = True

    if not found:
        print("No matching note found.")

def delete_all_notes():
    with open("notes.txt", "w") as file:
        pass

    print("All notes deleted successfully!")


while True:
    print("\n📝 Welcome to Notes Manager")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Search Note")
    print("4. Delete All Notes")
    print("5. Exit")

    choice = input("Enter choice(1/2/3/4/5): ")

    if choice == '1':
        add_note()

    elif choice == '2':
        view_note()

    elif choice == "3":
        search_note()

    elif choice == "4":
        delete_all_notes()

    elif choice == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid choice")