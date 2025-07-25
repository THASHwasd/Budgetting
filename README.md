Personal Expense Tracker
Author: Thash Kunarajah

A simple command-line expense tracking application written in Python. This is a very borderline implementation that provides basic functionality for tracking personal expenses.

⚠️ Important Notice
While this application can be used out of the box, it is highly recommended to adapt it to your personal needs. The current implementation is basic and may not cover all use cases or edge scenarios you might encounter in real-world usage.

# Run the application
.py file

Features
✅ Add new expenses with date, category, and amount
✅ View all recorded expenses
✅ Remove specific expenses
✅ Simple command-line interface
✅ In-memory storage (data is lost when program exits)

Prerequisites
Python 3.6 or higher

Usage Examples
Adding an Expense
Add Expense

Enter Date (DD/MM/YYYY): 25/06/2025
Enter Category: Groceries
Enter total Groceries expense on 25/06/2025: 
45.50
Expense added successfully!
Viewing All Expenses
All Expenses:
{'Date': '25/06/2025', 'Category': 'Groceries', 'Spend': 45.5}
{'Date': '24/06/2025', 'Category': 'Transport', 'Spend': 12.0}
Removing an Expense
Date of Log: 25/06/2025
Catergory of Log: Groceries
Spend of Log: 45.5
Expense deleted.
Code Structure
The application consists of:

total_expenses: Global list storing all expense records
add_expense(): Function to capture new expense details
main(): Main program loop with menu system
Suggested Improvements
To make this more production-ready, consider implementing:

Data Persistence
python
# Save to CSV file
import csv

def save_to_csv():
    with open('expenses.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Date', 'Category', 'Spend'])
        writer.writeheader()
        writer.writerows(total_expenses)
Input Validation
python
def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False
Better Expense Search
python
def find_expenses_by_category(category):
    return [exp for exp in total_expenses if exp['Category'].lower() == category.lower()]
Spending Analysis
python
def get_total_by_category():
    categories = {}
    for exp in total_expenses:
        cat = exp['Category']
        categories[cat] = categories.get(cat, 0) + exp['Spend']
    return categories
Contributing
Feel free to fork this repository and submit pull requests for improvements. Some areas that would benefit from enhancement:

X Data persistence (CSV, JSON, or database)
X Better input validation and error handling
X Expense categorization and filtering
X Data visualization and reporting
X Configuration file support
X Unit tests

License
This project is open source. Feel free to use and modify according to your needs.

Disclaimer
This is a basic implementation intended for learning purposes. For production use or handling sensitive financial data, additional security measures and robust error handling should be implemented.

Remember: Adapt this code to fit your specific requirements before using it for serious expense tracking!

