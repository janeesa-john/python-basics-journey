# Expense Tracker
# Add, view, total, and delete expenses using Python

expenses = []


def add_expense():
    item = input("Enter item: ")

    while True:
        amount = input("Enter amount: ")

        if amount.isdigit():
            amount = int(amount)
            break
        else:
            print("Enter numbers only")

    expenses.append({"item": item, "amount": amount})
    print("Expense added successfully")


def view_expenses():
    if not expenses:
        print("No expenses found")
    else:
        print("\nSaved Expenses:")
        for i, expense in enumerate(expenses, start=1):
            print(i, ".", expense["item"], "- Rs.", expense["amount"])


def total_expense():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Spent: Rs.", total)


def delete_expense():
    if not expenses:
        print("No expenses found")
        return

    view_expenses()

    num = input("Enter expense number to delete: ")

    if not num.isdigit():
        print("Invalid input")
        return

    num = int(num)

    if 1 <= num <= len(expenses):
        expenses.pop(num - 1)
        print("Expense deleted successfully")
    else:
        print("Invalid expense number")


while True:
    print("\n💸 Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spent")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")