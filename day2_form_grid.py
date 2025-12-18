import tkinter as tk

root = tk.Tk()
root.title("Day 2 – Grid Form")
root.geometry("400x200")

# labels
tk.Label(root, text="First name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Last name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")

# entries
first_entry = tk.Entry(root, width=25)
first_entry.grid(row=0, column=1, padx=10, pady=5)

last_entry = tk.Entry(root, width=25)
last_entry.grid(row=1, column=1, padx=10, pady=5)

def show_full_name():
    full_name = first_entry.get() + " " + last_entry.get()
    print("Full name:", full_name)

submit_button = tk.Button(root, text="Submit", command=show_full_name)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
"""
Step 3: Your mini-task
Make day2_greeter.py that:

Asks for a name and favorite language (two Entry fields, two Labels).

Uses grid() for layout with 2 rows of labels+entries and a “Greet me” button
in row 2 spanning both columns.

On click, prints something like: Hello <name>,
nice to see a <language> developer here! in the console using .get() on both entries.   """

