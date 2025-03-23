# Expense Tracker CLI Application
# Check It : https://roadmap.sh/projects/expense-tracker

## Overview
The **Expense Tracker CLI Application** is a simple yet powerful tool that allows users to track their daily expenses efficiently. It provides features to add, update, delete, view, summarize, and export expenses in a structured format.

## Features
- **Add Expenses**: Store expenses with a description, amount, category, and date.
- **Update Expenses**: Modify existing expense records.
- **Delete Expenses**: Remove unwanted expense entries.
- **View Expenses**: Display all expenses or filter them by category.
- **Summarize Expenses**: View total expenses, optionally filtering by month.
- **Export Expenses**: Save expense data as a CSV file for external use.

---

## Installation
### **Prerequisites**
- Python 3.x must be installed on your system.
- Required modules: `argparse`, `json`, `os`, `csv`, `datetime` (all are built-in Python modules).

### **Clone the Repository**
```sh
git clone https://github.com/Nathishwar-prog/expense-tracker.git
cd expense-tracker
```

### **Run the Application**
Use the command-line interface to interact with the script:
```sh
python expense_tracker.py [command] [arguments]
```

---

## Usage Guide

### **1. Add a New Expense**
```sh
python expense_tracker.py add "Lunch" 200 "Food"
```
**Example Output:**
```
New Expense Added!
```

### **2. Update an Existing Expense**
```sh
python expense_tracker.py update 1 "Dinner" 250 "Food"
```
**Example Output:**
```
Expense Updated!
```

### **3. Delete an Expense**
```sh
python expense_tracker.py delete 1
```
**Example Output:**
```
Expense Deleted Successfully!
```

### **4. View All Expenses**
```sh
python expense_tracker.py view-expenses
```

### **5. View Expenses by Category**
```sh
python expense_tracker.py view-expenses "Food"
```

### **6. View Summary (Total Expenses)**
```sh
python expense_tracker.py summary
```

### **7. View Summary for a Specific Month (e.g., March)**
```sh
python expense_tracker.py summary --month 3
```

### **8. Export Expenses to CSV**
```sh
python expense_tracker.py export
```
**Example Output:**
```
Exported as CSV file successfully!
```

---

## File Structure
```
expense-tracker/
│── expense_tracker.py     # Main script file
│── expense.json           # Stores expense data
│── expenses.csv           # Exported CSV file (if exported)
│── README.md              # Documentation
```



## Contributors
- **Nathishwar** -> https://github.com/Nathishwar-prog

## License
This project is licensed under the **MIT License**.

