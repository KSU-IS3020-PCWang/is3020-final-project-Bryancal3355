"""
PocketLedger - A command-line personal budget and expense tracker.

Lets a user log transactions, categorize spending, check remaining
budget, and save/load data from a CSV file so records persist
between sessions.
"""

import csv
import os

DATA_FILE = os.path.join("data", "transactions.csv")
FIELDNAMES = ["date", "description", "amount", "category"]


def load_transactions():
    """Read transactions.csv into a list of dictionaries.

    Returns an empty list if the file does not exist yet, which
    happens the first time the program is run.
    """
    transactions = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["amount"] = float(row["amount"])
                transactions.append(row)
    return transactions


def save_transactions(transactions):
    """Write the current list of transactions out to transactions.csv."""
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(transactions)


def get_valid_amount(prompt):
    """Repeatedly prompt until the user enters a valid, non-negative number."""
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Amount cannot be negative. Please try again.")
                continue
            return amount
        except ValueError:
            print("Invalid amount. Please enter a number.")


def add_transaction(transactions):
    """Prompt the user for transaction details and add a new record."""
    date = input("Enter date (MM/DD/YYYY): ").strip()
    description = input("Enter description: ").strip()
    amount = get_valid_amount("Enter amount: ")
    category = input("Enter category: ").strip()

    transaction = {
        "date": date,
        "description": description,
        "amount": amount,
        "category": category
    }
    transactions.append(transaction)
    save_transactions(transactions)
    print("Transaction added.")


def view_transactions(transactions):
    """Print every recorded transaction in a readable, numbered table."""
    if not transactions:
        print("No transactions recorded yet.")
        return

    print("\n{:<4}{:<12}{:<25}{:<10}{:<15}".format(
        "#", "Date", "Description", "Amount", "Category"))
    print("-" * 66)
    for i, t in enumerate(transactions, start=1):
        print("{:<4}{:<12}{:<25}{:<10.2f}{:<15}".format(
            i, t["date"], t["description"], t["amount"], t["category"]))


def calculate_category_totals(transactions):
    """Sum spending per category and display the totals."""
    totals = {}
    for t in transactions:
        category = t["category"]
        totals[category] = totals.get(category, 0) + t["amount"]

    if not totals:
        print("No transactions to summarize.")
        return

    print("\nCategory Totals:")
    for category, total in totals.items():
        print(f"{category}: ${total:.2f}")


def check_budget_status(transactions, budget):
    """Compare total spending against the monthly budget and report status."""
    total_spent = sum(t["amount"] for t in transactions)
    remaining = budget - total_spent

    print(f"\nTotal spent: ${total_spent:.2f}")
    print(f"Monthly budget: ${budget:.2f}")
    if remaining >= 0:
        print(f"You have ${remaining:.2f} remaining this month.")
    else:
        print(f"You are over budget by ${abs(remaining):.2f}.")


def get_valid_index(transactions, prompt):
    """Prompt for a 1-based transaction number and return its 0-based index,
    or None if the input was invalid or out of range."""
    try:
        index = int(input(prompt)) - 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

    if 0 <= index < len(transactions):
        return index

    print("Invalid transaction number.")
    return None


def delete_transaction(transactions):
    """Remove a transaction chosen by its position in the list."""
    if not transactions:
        print("No transactions to delete.")
        return

    view_transactions(transactions)
    index = get_valid_index(
        transactions, "\nEnter the number of the transaction to delete: ")
    if index is not None:
        removed = transactions.pop(index)
        save_transactions(transactions)
        print(f"Deleted: {removed['description']} (${removed['amount']:.2f})")


def edit_transaction(transactions):
    """Update the amount, category, or description of an existing transaction.

    Leaving a field blank keeps its current value.
    """
    if not transactions:
        print("No transactions to edit.")
        return

    view_transactions(transactions)
    index = get_valid_index(
        transactions, "\nEnter the number of the transaction to edit: ")
    if index is None:
        return

    t = transactions[index]
    print("Leave a field blank to keep its current value.")

    new_description = input(f"Description [{t['description']}]: ").strip()
    if new_description:
        t["description"] = new_description

    new_amount = input(f"Amount [{t['amount']:.2f}]: ").strip()
    if new_amount:
        try:
            t["amount"] = float(new_amount)
        except ValueError:
            print("Invalid amount entered. Keeping original amount.")

    new_category = input(f"Category [{t['category']}]: ").strip()
    if new_category:
        t["category"] = new_category

    save_transactions(transactions)
    print("Transaction updated.")


def get_budget():
    """Prompt the user for their monthly budget amount."""
    return get_valid_amount("Enter your monthly budget: ")


def main_menu():
    """Display the menu in a loop and route user choices to the right function."""
    transactions = load_transactions()
    budget = get_budget()

    menu_actions = {
        "1": lambda: add_transaction(transactions),
        "2": lambda: view_transactions(transactions),
        "3": lambda: calculate_category_totals(transactions),
        "4": lambda: check_budget_status(transactions, budget),
        "5": lambda: delete_transaction(transactions),
        "6": lambda: edit_transaction(transactions),
    }

    while True:
        print("\n--- PocketLedger Menu ---")
        print("1. Add transaction")
        print("2. View transactions")
        print("3. View category totals")
        print("4. Check budget status")
        print("5. Delete transaction")
        print("6. Edit transaction")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break
        elif choice in menu_actions:
            menu_actions[choice]()
        else:
            print("Invalid option. Please choose 1-7.")


if __name__ == "__main__":
    main_menu()