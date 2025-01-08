import pandas as pd

class BudgetTracker:
    def __init__(self):
        self.income = 0
        self.expenses = {}
        self.balance = 0

    def add_income(self, amount):
        if amount < 0:
            print("Income amount cannot be negative.")
            return
        self.income += amount
        self.balance += amount
        print(f"Added income: ${amount}")

    def add_expense(self, category, amount):
        if amount < 0:
            print("Expense amount cannot be negative.")
            return
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        self.balance -= amount
        print(f"Added expense: ${amount} to category '{category}'")

    def get_balance(self):
        return self.balance

    def get_expenses(self):
        return self.expenses

    def get_income(self):
        return self.income

    def display_summary(self):
        print("\n--- Budget Summary ---")
        print(f"Total Income: ${self.income}")
        print("Expenses:")
        for category, amount in self.expenses.items():
            print(f"  {category}: ${amount}")
        print(f"Balance: ${self.balance}")

    def export_to_excel(self, filename):
        data = {
            'Category': list(self.expenses.keys()) + ['Income', 'Balance'],
            'Amount': list(self.expenses.values()) + [self.income, self.balance]
        }
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        print(f"Data exported to {filename}")

def main():
    tracker = BudgetTracker()
    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Get Balance")
        print("4. Get Expenses")
        print("5. Get Income")
        print("6. Display Summary")
        print("7. Export to Excel")
        print("8. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            try:
                amount = float(input("Enter income amount: $"))
                tracker.add_income(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "2":
            category = input("Enter expense category: ")
            try:
                amount = float(input("Enter expense amount: $"))
                tracker.add_expense(category, amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "3":
            print("Balance: $", tracker.get_balance())
        elif choice == "4":
            print("Expenses: ")
            for category, amount in tracker.get_expenses().items():
                print(f"{category}: ${amount}")
        elif choice == "5":
            print("Income: $", tracker.get_income())
        elif choice == "6":
            tracker.display_summary()
        elif choice == "7":
            filename = input("Enter filename to export (e.g., budget.xlsx): ")
            tracker.export_to_excel(filename)
        elif choice == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()