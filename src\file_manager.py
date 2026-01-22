
import csv
import os
from src.expense import Expense

DATA_FILE = "data/expenses.csv"
BACKUP_FILE = "backup/expenses_backup.csv"

def load_expenses():
    expenses = []
    if not os.path.exists(DATA_FILE):
        return expenses

    with open(DATA_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(
                Expense(row['Date'], row['Category'], row['Amount'], row['Description'])
            )
    return expenses

def save_expenses(expenses):
    os.makedirs("data", exist_ok=True)   # ✅ CREATE FOLDER IF NOT EXISTS

    with open(DATA_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])
        for exp in expenses:
            writer.writerow(exp.to_list())


def backup_data():
    if not os.path.exists(DATA_FILE):
        return False
    os.makedirs("backup", exist_ok=True)
    with open(DATA_FILE, 'r') as src, open(BACKUP_FILE, 'w') as dst:
        dst.write(src.read())
    return True

def restore_data():
    if not os.path.exists(BACKUP_FILE):
        return False
    with open(BACKUP_FILE, 'r') as src, open(DATA_FILE, 'w') as dst:
        dst.write(src.read())
    return True
