import tkinter as tk

def add_digit(digit):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + digit)

def clear_display():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("/", 4, 3)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, padx=40, pady=20, command=lambda text=text: add_digit(text) if text != "=" else calculate())
    button.grid(row=row, column=column)

root.mainloop()
