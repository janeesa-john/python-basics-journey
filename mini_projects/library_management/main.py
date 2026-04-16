# Library Management System using Python
# Manage books with add, search, update, display, and delete features

library = []

def add_book():
    book = {}
    while True:
        book['id'] = input("Enter book id: ")
        if book['id'].isdigit():
            book['id'] = int(book['id'])
            for b in library:
                if b['id'] == book['id']:
                    print("Book ID already exists")
                    return
            break
        else:
            print("Invalid id. Numbers only")

    book['title'] = input("Enter book title: ").lower()

    while True:
        book['price'] = input("Enter book price: ")
        if book['price'].isdigit():
            book['price'] = int(book['price'])
            break
        else:
            print("Invalid price. Numbers only")

    library.append(book)
    print("Book added successfully")

def search_book():
    search = input("Enter book id: ")
    if search.isdigit():
        search = int(search)
    else:
        print("Invalid id")
        return

    for book in library:
        if book['id'] == search:
            print("\nBook found")
            print("ID: ", book['id'])
            print("Title: ", book['title'].title())
            print("Price: Rs.", book['price'])
            return
    else:
        print("Book not found")

def display_books():
    if not library:
        print("Library empty")
    else:
        print("\nBooks in Library:")
        for book in library:
            print(book['id'], '-', book['title'].title(), '-Rs.', book['price'])

def update_book():
    update = input("Enter book id: ")
    if update.isdigit():
        update = int(update)
    else:
        print("Invalid id")
        return

    for book in library:
        if book['id'] == update:
            print(f"{book['id']} - {book['title']} - {book['price']}")
            while True:
                update_price = input("Enter updated price: ")
                if update_price.isdigit():
                    book['price'] = int(update_price)
                    print(f"{book['id']} - {book['title']} - {book['price']}")
                    print("Price updated successfully")
                    return
                else:
                    print("Invalid price")
    else:
        print("Book not found")

def delete_book():
    delete = input("Enter book id to delete: ")

    if delete.isdigit():
        delete = int(delete)
    else:
        print("Invalid id")
        return

    for book in library:
        if book['id'] == delete:
            library.remove(book)
            print("Book removed successfully")
            return
    else:
        print("Book id not found")

while True:
    print("\n📚 Library Management System")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Display Books")
    print("4. Update Book Price")
    print("5. Delete Book")
    print("6. Exit")
    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        search_book()
    elif choice == '3':
        display_books()
    elif choice == '4':
        update_book()
    elif choice == '5':
        delete_book()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice")