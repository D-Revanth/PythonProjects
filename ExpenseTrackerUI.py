import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json

# File to store expenses
EXPENSES_FILE = "expenses.json"

# List to store expense records
expenses = []

# Predefined categories with "All" as the default option
categories = ["All", "Food", "Transport", "Entertainment", "Bills", "Shopping", "Others"]

# Function to load expenses from file
def load_expenses():
    try:
        with open(EXPENSES_FILE, "r") as file:
            global expenses
            expenses = json.load(file)
            update_expense_list()
    except FileNotFoundError:
        with open(EXPENSES_FILE, "w") as file:
            json.dump(expenses, file)

# Function to save expenses to file
def save_expenses():
    with open(EXPENSES_FILE, "w") as file:
        json.dump(expenses, file)

# Function to add a new expense
def add_expense():
    try:
        amount = float(entry_amount.get())
        category = category_var.get()
        date = entry_date.get()
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid date in YYYY-MM-DD format.")
            return
        if category == "All":
            messagebox.showerror("Input Error", "Please select a valid category.")
            return
        expense = {'amount': amount, 'category': category, 'date': date}
        expenses.append(expense)
        save_expenses()
        update_expense_list()
        entry_amount.delete(0, tk.END)
        entry_date.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for the amount.")

# Function to remove the selected expense
def remove_expense():
    selected_index = listbox_expenses.curselection()
    if not selected_index:
        messagebox.showwarning("Selection Error", "Please select an expense to remove.")
        return
    expenses.pop(selected_index[0])
    save_expenses()
    update_expense_list()

# Function to update the listbox with current expenses
def update_expense_list(filtered_expenses=None):
    listbox_expenses.delete(0, tk.END)
    total_expense = 0
    for expense in filtered_expenses or expenses:
        listbox_expenses.insert(tk.END, f"{expense['date']} - {expense['category']} - ₹{expense['amount']}")
        total_expense += expense['amount']
    label_total.config(text=f"Total Expenses: ₹{total_expense:.2f}")

def show_expenses_by_category():
    selected_category = category_summary_var.get()
    print(f"Selected Category: {selected_category}")
    if selected_category == "All":
        filtered_expenses = expenses
        print(f"Filtered Expenses: {filtered_expenses}")
        update_expense_list(filtered_expenses)
    else:
        filtered_expenses1 = [expense for expense in expenses if expense['category'] == selected_category]
        print(f"Filtered Expenses: {filtered_expenses1}")
        update_expense_list(filtered_expenses1)


# Create the main window
root = tk.Tk()
root.title("Expense Tracker")

# Set window size and center the window on the screen
window_width = 400
window_height = 650
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
root.resizable(False, False)  # Disable window resizing

# Set color scheme and font
bg_color = "#f7f7f7"
fg_color = "#333333"
button_color = "#4CAF50"
font = ("Helvetica", 12)

root.configure(bg=bg_color)

# Frame for Entry fields and buttons
frame_top = tk.Frame(root, bg=bg_color)
frame_top.pack(pady=10)

# Label and Entry for Amount
label_amount = tk.Label(frame_top, text="Enter the amount:", bg=bg_color, fg=fg_color, font=font)
label_amount.grid(row=0, column=0, padx=5, pady=5, sticky="e")

entry_amount = tk.Entry(frame_top, font=font)
entry_amount.grid(row=0, column=1, padx=5, pady=5)

# Label and Entry for Date
label_date = tk.Label(frame_top, text="Enter the date (YYYY-MM-DD):", bg=bg_color, fg=fg_color, font=font)
label_date.grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry_date = tk.Entry(frame_top, font=font)
entry_date.grid(row=1, column=1, padx=5, pady=5)

# Label and OptionMenu for Category
label_category = tk.Label(frame_top, text="Select a category:", bg=bg_color, fg=fg_color, font=font)
label_category.grid(row=2, column=0, padx=5, pady=5, sticky="e")

category_var = tk.StringVar(value=categories[1])
category_menu = tk.OptionMenu(frame_top, category_var, *categories)
category_menu.grid(row=2, column=1, padx=5, pady=5)

# Buttons for Add and Remove
button_add = tk.Button(frame_top, text="Add Expense", bg=button_color, fg="white", font=font, width=15, command=add_expense)
button_add.grid(row=3, column=0, padx=5, pady=10, columnspan=2)

button_remove = tk.Button(frame_top, text="Remove Selected Expense", bg="#e74c3c", fg="white", font=font, width=20, command=remove_expense)
button_remove.grid(row=4, column=0, padx=5, pady=10, columnspan=2)

# Frame for Listbox
frame_listbox = tk.Frame(root, bg=bg_color)
frame_listbox.pack(pady=10)

# Listbox to display expenses
listbox_expenses = tk.Listbox(frame_listbox, height=10, width=50, font=("Helvetica", 10), fg=fg_color)
listbox_expenses.pack(side="left", fill="y")

# Add a scrollbar to the Listbox
scrollbar = tk.Scrollbar(frame_listbox, orient="vertical")
scrollbar.config(command=listbox_expenses.yview)
scrollbar.pack(side="right", fill="y")

listbox_expenses.config(yscrollcommand=scrollbar.set)

# Label for Total Expenses
label_total = tk.Label(root, text="Total Expenses: ₹0.00", bg=bg_color, fg=fg_color, font=("Helvetica", 14, "bold"))
label_total.pack(pady=10)

# Frame for category summary
frame_summary = tk.Frame(root, bg=bg_color)
frame_summary.pack(pady=10)

label_summary = tk.Label(frame_summary, text="Check expenses by category:", bg=bg_color, fg=fg_color, font=font)
label_summary.grid(row=0, column=0, padx=5, pady=5, sticky="e")

category_summary_var = tk.StringVar(value=categories[0])  # Default to "All"
category_summary_menu = tk.OptionMenu(frame_summary, category_summary_var, *categories)
category_summary_menu.grid(row=0, column=1, padx=5, pady=5)

button_summary = tk.Button(frame_summary, text="Show", bg=button_color, fg="white", font=font, command=show_expenses_by_category)
button_summary.grid(row=1, column=0, padx=5, pady=10, columnspan=2)

# Load existing expenses from file
load_expenses()

# Start the Tkinter main loop
root.mainloop()
