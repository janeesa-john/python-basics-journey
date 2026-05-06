def add_note():
    note = input("Enter note: ")

    if note.strip() == "":
        print("Note cannot be empty")
        return

    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    print("Note added successfully!")


def view_note():
    with open("notes.txt", "r") as file:
        notes = file.readlines()

    if not notes:
        print("No notes found.")
    else:
        print("\nSaved Notes:")

        for index, note in enumerate(notes, start=1):
            print(index, ".", note.strip())

        print("\nTotal notes:", len(notes))


def search_note():
    keyword = input("Enter keyword to search: ").lower()

    with open("notes.txt", "r") as file:
        found = False

        print("\nSearch Results:")

        for line in file:
            if keyword in line.lower():
                print(line.strip())
                found = True

    if not found:
        print("No matching note found.")


def delete_note():
    with open("notes.txt", "r") as file:
        notes = file.readlines()

    if not notes:
        print("No notes to delete.")
        return

    print("\nSaved Notes:")

    for index, note in enumerate(notes, start=1):
        print(index, ".", note.strip())

    num = int(input("Enter note number to delete: "))

    if num < 1 or num > len(notes):
        print("Invalid note number.")
        return

    notes.pop(num - 1)

    with open("notes.txt", "w") as file:
        file.writelines(notes)

    print("Note deleted successfully!")


def delete_all_notes():
    confirm = input("Are you sure you want to delete all notes? (yes/no): ").lower()

    if confirm != "yes":
        print("Operation cancelled.")
        return

    with open("notes.txt", "w") as file:
        pass

    print("All notes deleted successfully!")


print("📝 Welcome to Notes Manager")

while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Search Note")
    print("4. Delete Single Note")
    print("5. Delete All Notes")
    print("6. Exit")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice == '1':
        add_note()

    elif choice == '2':
        view_note()

    elif choice == '3':
        search_note()

    elif choice == '4':
        delete_note()

    elif choice == '5':
        delete_all_notes()

    elif choice == '6':
        print("Goodbye!")
        break

    else:
        print("Invalid choice")