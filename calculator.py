import tkinter as tk

# Function to perform calculations
def calculate(operation):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Configure the main window
window = tk.Tk()
window.title("Calculator")

# Text entry
entry = tk.Entry(window, width=20, font=("Arial", 18), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for text, row, column in buttons:
    if text == "=":
        command = lambda op=text: calculate(op)
    elif text == "C":
        command = lambda: entry.delete(0, tk.END)
    else:
        command = lambda num=text: entry.insert(tk.END, num)
    tk.Button(window, text=text, width=5, height=2, command=command).grid(row=row, column=column)

# Start the GUI loop
window.mainloop()
