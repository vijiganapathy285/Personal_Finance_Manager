from datetime import datetime

def validate_amount(value):
    try:
        amt = float(value)
        if amt <= 0:
            raise ValueError
        return amt
    except ValueError:
        raise ValueError("Amount must be a positive number")

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")

def validate_category(category):
    categories = ["Food", "Transport", "Entertainment", "Shopping", "Other"]
    if category not in categories:
        raise ValueError(f"Category must be one of {categories}")
    return category
