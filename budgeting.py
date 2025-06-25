#!/usr/bin/env python3
"""
Personal Expense Tracker

A simple command-line application for tracking personal expenses.
Author: Thash Kunarajah

This is a basic implementation suitable for learning purposes.
For production use, consider adding data persistence and enhanced validation.
"""

import csv
import time

# Global list to store expenses
total_expenses = []

def add_expense():
    """
    Prompts user for expense details and creates an expense dictionary.
    
    Returns:
        dict: Dictionary containing Date, Category, and Spend keys
    """
    print("Add Expense\n")
    date = input("Enter Date (DD/MM/YYYY): ")
    category = input("Enter Category: ")
    print(f"Enter total {category} expense on {date}: ")
    spend = float(input())

    # Create a dictionary for the expense
    expense = {"Date": date, "Category": category, "Spend": spend}
    return expense

def main():
    """
    Main program loop that handles user menu interactions.
    Provides options to add, view, remove expenses, or exit.
    """
    while True:
        time.sleep(1.5)
        print("------------------------")
        print("\nExpense Tracker: \n")
        print("(1) Add Expense")
        print("(2) View All Expenses")
        print("(3) Remove Expense")
        print("(4) Exit")
        print("------------------------")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Add an expense and store it in the global list
            expense = add_expense()
            total_expenses.append(expense)
            print("Expense added successfully!")

        elif choice == 2:
            # Display all expenses
            print("\nAll Expenses:")
            if len(total_expenses) == 0:
                print(" -List Empty-")
            else:    
                for exp in total_expenses:  # Loop through all expenses
                    print(exp)

        elif choice == 3:
            # Remove expense by matching all fields
            if len(total_expenses) == 0:
                print (" -List Already Empty")
            else:
                # Get details of expense to delete
                delete_opt_date = input("Date of Log: ")
                delete_opt_cat = input("Catergory of Log: ")
                delete_opt_spd = input("Spend of Log: ")
            
                # Search for matching expense
                for expense in total_expenses:
                    if (expense["Date"] == delete_opt_date and 
                    expense["Category"] == delete_opt_cat and 
                    expense["Spend"] == delete_opt_spd):
                        total_expenses.remove(expense)
                        print("Expense deleted.")
                        return total_expenses  # Return the updated list
                    else:
                        print("No matching expense found.")
                        return total_expenses

        elif choice == 4:
            # Exit the program
            print("Goodbye!")
            break
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
