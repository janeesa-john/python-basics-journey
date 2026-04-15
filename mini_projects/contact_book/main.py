print("📒 Welcome to Contact Book")

contact_book = {}

def add_contact():
    name = input("Enter name: ")
    number = input("Enter contact number: ")

    if name in contact_book:
        print("Contact already exists")
    else:
        contact_book[name] = number
        print("Contact added successfully")


def view_contacts():
    if not contact_book:
        print("No contacts found")
    else:
        print("\nSaved Contacts:")
        for name, number in contact_book.items():
            print(name, "-", number)


def search_contact():
    search = input("Enter name to search: ")

    if search in contact_book:
        print(search, "-", contact_book[search])
    else:
        print("Contact not found")


def delete_contact():
    delete = input("Enter name to delete: ")

    if delete in contact_book:
        del contact_book[delete]
        print("Contact deleted successfully")
    else:
        print("Contact not found")


def update_contact():
    name = input("Enter contact name to update: ")

    if name in contact_book:
        number = input("Enter new contact number: ")
        contact_book[name] = number
        print("Contact updated successfully")
    else:
        print("Contact not found")


while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        update_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
