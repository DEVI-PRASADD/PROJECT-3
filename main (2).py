import json
from datetime import datetime

# Expense Tracker Class
class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    # Load expenses from file
    def load_expenses(self):
        try:
            with open(self.filename, 'r') as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []
        except json.JSONDecodeError:
            print("Error decoding the file.")
            self.expenses = []

    # Save expenses to file
    def save_expenses(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.expenses, file, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    # Add an expense
    def add_expense(self, amount, description, category):
        try:
            amount = float(amount)
            date = datetime.now().strftime("%Y-%m-%d")
            expense = {"amount": amount, "description": description, "category": category, "date": date}
            self.expenses.append(expense)
            self.save_expenses()
            print("Expense added successfully!")
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.")

    # View all expenses
    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            for exp in self.expenses:
                print(f"Amount: {exp['amount']} | Description: {exp['description']} | Category: {exp['category']} | Date: {exp['date']}")

    # View expenses by category
    def view_expenses_by_category(self, category):
        filtered_expenses = [exp for exp in self.expenses if exp['category'].lower() == category.lower()]
        if not filtered_expenses:
            print(f"No expenses found for category '{category}'.")
        else:
            for exp in filtered_expenses:
                print(f"Amount: {exp['amount']} | Description: {exp['description']} | Date: {exp['date']}")

    # View monthly summary
    def view_monthly_summary(self, month):
        monthly_expenses = [exp for exp in self.expenses if exp['date'].startswith(month)]
        if not monthly_expenses:
            print(f"No expenses found for month '{month}'.")
        else:
            total_spent = sum(exp['amount'] for exp in monthly_expenses)
            print(f"Total spent in {month}: {total_spent}")
            for exp in monthly_expenses:
                print(f"Amount: {exp['amount']} | Description: {exp['description']} | Category: {exp['category']}")

# Main Function
def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. View Monthly Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount = input("Enter amount: ")
            description = input("Enter description: ")
            category = input("Enter category (e.g., food, transport, etc.): ")
            tracker.add_expense(amount, description, category)

        elif choice == '2':
            tracker.view_expenses()

        elif choice == '3':
            category = input("Enter category to filter by: ")
            tracker.view_expenses_by_category(category)

        elif choice == '4':
            month = input("Enter month (YYYY-MM): ")
            tracker.view_monthly_summary(month)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
