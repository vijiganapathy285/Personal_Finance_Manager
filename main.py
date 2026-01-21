
from src.file_manager import load_expenses, backup_data, restore_data
from src.menu import show_menu, add_expense
from src.reports import category_summary, generate_monthly_report

def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            for exp in expenses:
                print(exp)

        elif choice == "3":
            summary = category_summary(expenses)
            for cat, amt in summary.items():
                print(f"{cat:<15} : ₹{amt:.2f}")

        elif choice == "4":
            month = input("Enter month (YYYY-MM): ")
            total, report = generate_monthly_report(expenses, month)
            print("\n".join(report))
            print(f"\nTotal spent: ₹{total:.2f}")

        elif choice == "5":
            print("Backup successful!" if backup_data() else "No data to backup.")

        elif choice == "6":
            print("Restore successful!" if restore_data() else "No backup found.")

        elif choice == "7":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
