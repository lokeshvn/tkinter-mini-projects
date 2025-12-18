import tkinter as tk

root = tk.Tk()
root.title("Day 5 – Simple Calculator")
root.geometry("300x480")     # tall enough so row 5 is visible
root.resizable(False, False)

display = tk.Entry(root, font=("Segoe UI", 16), justify="right", bd=5, relief="sunken")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=8)

current_expression = ""


def update_display(value):
    global current_expression
    current_expression += str(value)
    display.delete(0, tk.END)
    display.insert(0, current_expression)


def clear_display():
    global current_expression
    current_expression = ""
    display.delete(0, tk.END)


def calculate_result():
    global current_expression
    if not current_expression:
        return
    try:
        result = eval(current_expression)
        display.delete(0, tk.END)
        display.insert(0, str(result))
        current_expression = str(result)
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        current_expression = ""


buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
]

for (text, r, c) in buttons:
    if text == "C":
        cmd = clear_display
    else:
        cmd = lambda v=text: update_display(v)

    tk.Button(
        root,
        text=text,
        width=5,
        height=2,
        font=("Segoe UI", 12),
        command=cmd
    ).grid(row=r, column=c, padx=5, pady=5)

# this is the = button
equals_button = tk.Button(
    root,
    text="=",
    width=24,          # wide button
    height=2,
    font=("Segoe UI", 12),
    command=calculate_result
)
equals_button.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

root.bind("<Return>", lambda event: calculate_result())

root.mainloop()
