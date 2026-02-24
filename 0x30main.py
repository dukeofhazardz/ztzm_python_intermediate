import json
import os
from collections import defaultdict

FILE_NAME = "budget.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_transaction():
    print("> Add Transaction")
    amount = float(input("Amount: "))
    category = input("Category: ")
    t_type = input("Type: ")

    transaction = {
        "amount": amount,
        "category": category,
        "type": t_type.capitalize()
    }

    data = load_data()
    data.append(transaction)
    save_data(data)

    print("Saved to file.\n")


def view_summary():
    print("> View Summary")

    data = load_data()
    if not data:
        print("No transactions found.\n")
        return

    income_total = 0
    expense_total = 0
    category_summary = defaultdict(float)

    for item in data:
        if item["type"] == "Income":
            income_total += item["amount"]
        elif item["type"] == "Expense":
            expense_total += item["amount"]

        category_summary[item["category"]] += item["amount"]

    print(f"\nTotal Income: {income_total}")
    print(f"Total Expenses: {expense_total}")
    print(f"Balance: {income_total - expense_total}\n")

    print("Category Breakdown:")
    for category, total in category_summary.items():
        print(f"{category}: {total}")
    print()


def main():
    while True:
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. Exit\n")

        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("Exiting Budget Tracker.")
            break
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()