import csv
from datetime import datetime

FILE_NAME = 'expenses.csv'

def add_expense(amount, category, note):
    date = datetime.now().strftime('%Y-%m-%d')
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, note])

def view_expenses():
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            print("Date\t\tAmount\tCategory\tNote")
            for row in reader:
                print('\t'.join(row))
    except FileNotFoundError:
        print("No expenses found.")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            note = input("Enter note: ")
            add_expense(amount, category, note)
            print("Expense added!")
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()