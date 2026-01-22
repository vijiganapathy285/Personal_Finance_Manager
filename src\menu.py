from src.expense import Expense
from src.utils import validate_amount, validate_date, validate_category
from src.file_manager import save_expenses, backup_data, restore_data
from src.reports import category_summary, generate_monthly_report


def show_menu():
    print("\n" + "=" * 42)
    print("     PERSONAL FINANCE MANAGER")
    print("=" * 42)
    print("""
1. Add New Expense
2. View All Expenses
3. Category-wise Summary
4. Monthly Report
5. Backup Data
6. Restore Data
7. Exit
""")

def add_expense(expenses):
    try:
        amount = validate_amount(input("Enter amount: "))
        category = validate_category(input("Enter category: "))
        date = validate_date(input("Enter date (YYYY-MM-DD): "))
        description = input("Enter description: ")

        expenses.append(Expense(amount, category, date, description))
        save_expenses(expenses)
        print("✅ Expense added successfully!")

    except ValueError as e:
        print(f"❌ Error: {e}")
