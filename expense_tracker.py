expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expense = [name, amount]
    expenses.append(expense)

    print("Expense added")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found")
    else:
        print("Expenses:")
        for expense in expenses:
            print(expense[0], "-", expense[1])


def total_expense():
    total = 0

    for expense in expenses:
        total = total + expense[1]

    print("Total expense =", total)


while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank you")
        break

    else:
        print("Invalid choice")
