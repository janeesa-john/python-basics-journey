

print("📒 Contact Book")

contact_book = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        number = input("Enter contact number: ")
        contact_book[name] = number
        print("Contact added successfully")

    elif choice == '2':
        if not contact_book:
            print("No contacts found")
        else:
            print("\nSaved contacts: ")
            for name,number in contact_book.items():
                print(name,"-",number)

    elif choice == '3':
        search = input("Enter name to search: ")
        if search in contact_book:
            print(search,'-',contact_book[search])
        else:
            print("Contact not found")

    elif choice == '4':
        delete = input("Enter name to delete: ")
        if delete in contact_book:
            del contact_book[delete]
            print("Contact deleted successfully")
        else:
            print("Contact not found")

    elif choice == '5':
        print("Good Bye!")
        break

    else:
        print("Invalid choice")
