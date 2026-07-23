import csv
import os

DATA_FILE = os.path.join("data", "transactions.csv")
FIELDNAMES = ["date", "description", "amount", "category"]


def load_transactions():
    transactions = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["amount"] = float(row["amount"])
                transactions.append(row)
    return transactions


def save_transactions(transactions):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(transactions)


def add_transaction(transactions):
    date = input("Enter date (MM/DD/YYYY): ")
    description = input("Enter description: ")

    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    category = input("Enter category: ")

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
    if not transactions:
        print("No transactions recorded yet.")
        return

    print("\n{:<12}{:<25}{:<10}{:<15}".format("Date", "Description", "Amount", "Category"))
    print("-" * 62)
    for i, t in enumerate(transactions):
        print("{:<12}{:<25}{:<10.2f}{:<15}".format(t["date"], t["description"], t["amount"], t["category"]))


def calculate_category_totals(transactions):
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
    total_spent = sum(t["amount"] for t in transactions)
    remaining = budget - total_spent

    print(f"\nTotal spent: ${total_spent:.2f}")
    print(f"Monthly budget: ${budget:.2f}")
    if remaining >= 0:
        print(f"You have ${remaining:.2f} remaining this month.")
    else:
        print(f"You are over budget by ${abs(remaining):.2f}.")


def delete_transaction(transactions):
    if not transactions:
        print("No transactions to delete.")
        return

    view_transactions(transactions)
    try:
        index = int(input("\nEnter the number of the transaction to delete (starting at 1): ")) - 1
        if 0 <= index < len(transactions):
            removed = transactions.pop(index)
            save_transactions(transactions)
            print(f"Deleted: {removed['description']} (${removed['amount']:.2f})")
        else:
            print("Invalid transaction number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def get_budget():
    while True:
        try:
            return float(input("Enter your monthly budget: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")


def main_menu():
    transactions = load_transactions()
    budget = get_budget()

    while True:
        print("\n--- PocketLedger Menu ---")
        print("1. Add transaction")
        print("2. View transactions")
        print("3. View category totals")
        print("4. Check budget status")
        print("5. Delete transaction")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            calculate_category_totals(transactions)
        elif choice == "4":
            check_budget_status(transactions, budget)
        elif choice == "5":
            delete_transaction(transactions)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main_menu()
