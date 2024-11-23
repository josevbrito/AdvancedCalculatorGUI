import tkinter as tk
from math import sin, cos, tan, log, exp, sqrt

# Function to process operations
def calculate(operation):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Functions for special operations
def add_function(function):
    try:
        value = entry.get()
        result = function(float(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Configure the main window
window = tk.Tk()
window.title("Advanced Calculator")
window.geometry("400x600")
window.config(bg="#2C3E50")

# Text entry
entry = tk.Entry(window, font=("Arial", 20), borderwidth=5, justify="right", bg="#ECF0F1", fg="#2C3E50")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
    ('(', 5, 0), (')', 5, 1), ('=', 5, 2), ('^', 5, 3),
]

# Function to insert text into the entry
def insert(value):
    entry.insert(tk.END, value)

# Create numeric and basic buttons
for text, row, col in buttons:
    if text == "=":
        command = lambda op=text: calculate(op)
    elif text == "C":
        command = clear
    elif text == "^":
        command = lambda: insert("**")
    else:
        command = lambda num=text: insert(num)
    tk.Button(window, text=text, width=5, height=2, command=command, font=("Arial", 14), bg="#34495E", fg="white").grid(row=row, column=col, padx=5, pady=5)

# Scientific buttons
functions = [
    ("sin", sin), ("cos", cos), ("tan", tan),
    ("log", log), ("exp", exp), ("√", sqrt),
]

for i, (name, function) in enumerate(functions):
    command = lambda f=function: add_function(f)
    tk.Button(window, text=name, width=5, height=2, command=command, font=("Arial", 14), bg="#1ABC9C", fg="white").grid(row=6 + i // 3, column=i % 3, padx=5, pady=5)

# Main loop
window.mainloop()
