import json
from datetime import date

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def show_menu():
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total")
    print("4. Delete expense")
    print("5. Exit")


def add_expense(expenses):
    description = input("Enter expense description: ").strip()
    category = input(
        "Enter category (Food, Transport, Shopping, Other): "
    ).strip()

    if not description:
        print("Description cannot be empty.")
        return

    if not category:
        category = "Other"

    try:
        amount = float(input("Enter expense amount: $"))
    except ValueError:
        print("Please enter a valid number.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    expense = {
        "description": description,
        "category": category,
        "amount": amount,
        "date": str(date.today()),
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\nYour Expenses")

    for index, expense in enumerate(expenses, start=1):
        category = expense.get("category", "Other")
        expense_date = expense.get("date", "No date")

        print(
            f"{index}. {expense['description']} "
            f"[{category}] - ${expense['amount']:.2f} "
            f"({expense_date})"
        )


def view_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total spent: ${total:.2f}")


def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses(expenses)

    try:
        expense_number = int(
            input("Enter the expense number to delete: ")
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    index = expense_number - 1

    if index < 0 or index >= len(expenses):
        print("Expense not found.")
        return

    deleted_expense = expenses.pop(index)
    save_expenses(expenses)

    print(
        f"Deleted: {deleted_expense['description']} - "
        f"${deleted_expense['amount']:.2f}"
    )


def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()