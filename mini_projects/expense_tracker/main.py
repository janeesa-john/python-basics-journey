expenses = []

def add_expense():
    item = input("Enter item: ")
    amount = int(input("Enter amount: "))

    expenses.append({"item": item, "amount": amount})
    print("Expense added successfully")


def view_expenses():
    if not expenses:
        print("No expenses found")
    else:
        for i, expense in enumerate(expenses, start=1):
            print(i, ".", expense["item"], "- Rs.", expense["amount"])


def total_expense():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Spent: Rs.", total)


while True:
    print("\n💸 Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spent")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")