# Personal_Finance_Manager
# 🧾 Personal Finance Manager (Python)

## 📌 Project Overview

The **Personal Finance Manager** is a beginner-friendly Python command-line application designed to help users track expenses, analyze spending patterns, and manage personal finances. The project follows **Object-Oriented Programming (OOP)** principles, uses **CSV file handling** for data persistence, and is organized with a **clean, modular structure** suitable for GitHub submission.

This project is ideal for **beginners** learning Python, OOP, file handling, and basic data analysis.

---

## 🎯 Project Objectives

* Track daily expenses with category, date, and description
* Store and retrieve data using CSV files
* Generate expense reports and summaries
* Implement strong error handling and validation
* Follow professional project structure and documentation standards

---

## 🛠 Project Options

### ✅ Option 1: Basic Version

* Add expenses
* View all expenses
* CSV data storage

### ✅ Option 2: Standard Version (Implemented)

* Expense tracking
* Category-wise and monthly reports
* Data backup and restore

### 🚀 Option 3: Advanced Version (Optional Extension)

* Charts using Matplotlib
* Budget planning
* Export reports (CSV / PDF)

---

## 📁 GitHub Repository Structure

```
personal-finance-manager/
│
├── README.md
├── main.py
├── requirements.txt
│
├── src/
│   ├── expense.py
│   ├── file_manager.py
│   ├── menu.py
│   ├── reports.py
│   └── utils.py
│
├── data/
│   └── expenses.csv
│
├── backup/
│   └── expenses_backup.csv
│
├── docs/
│   └── user_guide.md
│
├── tests/
│   └── test_expense.py
│
└── screenshots/
    └── menu.png
```

---

## ⚙️ Setup Instructions

### 1️⃣ Prerequisites

* Python 3.8 or above
* VS Code / any Python IDE

### 2️⃣ Installation Steps

```bash
git clone https://github.com/your-username/personal-finance-manager.git
cd personal-finance-manager
```

Create virtual environment (optional):

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python main.py
```

---

## 🧑‍💻 User Manual

### Main Menu Options

1. Add New Expense
2. View All Expenses
3. Category-wise Summary
4. Monthly Report
5. Backup Data
6. Restore Data
7. Exit

### Sample Input

```
Enter amount: 1500
Enter category: Food
Enter date: 2024-01-15
Enter description: Grocery shopping
```

---

## 📊 Sample Output

```
2024-01-15 | Food           | ₹1500.00 | Grocery shopping
```

---

## 🧠 Technical Details

### Architecture

* **OOP Design**: Expense represented as a class
* **Data Storage**: CSV using Python's `csv` module
* **Validation**: Input validation via utility functions
* **Reports**: Dictionary-based aggregation

### Data Structures Used

* Lists for storing expenses
* Dictionaries for category-wise summaries

---

## 🧪 Testing Evidence

Sample Test Case:

```python
def test_expense_amount():
    exp = Expense(100, 'Food', '2024-01-01', 'Test')
    assert exp.amount == 100
```

Manual testing performed for:

* Invalid input handling
* File not found scenarios
* Menu navigation

---

## ❗ Error Handling

* Invalid amount or date format
* Incorrect category input
* Missing data file handling
* Graceful exit on user errors

---

## 🖼 Visual Documentation

Screenshots of:

* Main menu
* Add expense flow
* Report output

(Stored in `/screenshots` folder)

---

## 📚 Tips for Beginners

* Start with Option 1 and build incrementally
* Use print statements for debugging
* Read error messages carefully
* Commit code regularly to GitHub
* Practice daily for consistency

---

## 📌 Future Enhancements

* GUI using Tkinter or Streamlit
* Graphical charts
* Cloud-based storage
* Mobile-friendly version

---

## 👩‍💻 Author

**Vijayalakshmi Ganapathy**
Beginner Python & Data Science Enthusiast

---


