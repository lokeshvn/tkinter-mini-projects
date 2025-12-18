##import tkinter as tk
##
##root = tk.Tk()
##
##root.title("Tkinter Day 1 – Widgets")
##root.geometry("600x400+300+150")
##root.resizable(False, True)
##root.configure(bg="#1e1e1e")  # optional styling
##
### --- first widget: a label ---
##title_label = tk.Label(
##    root,
##    text="Welcome to Tkinter Day 1",
##    font=("Segoe UI", 16, "bold"),
##    fg="white",
##    bg="#1e1e1e",
##)
##title_label.pack(pady=20)   # add some space around it
##
### --- second widget: a button ---
##ok_button = tk.Button(
##    root,
##    text="OK, Next Step",
##    font=("Segoe UI", 12),
##    padx=10,
##    pady=5,
##)
##ok_button.pack(pady=10)
##
##root.mainloop()
##




import tkinter as tk
from tkinter import messagebox  # built-in dialog boxes

root = tk.Tk()

root.title("Tkinter Day 1 – Events")
root.geometry("600x400+300+150")
root.resizable(False, True)
root.configure(bg="#1e1e1e")

title_label = tk.Label(
    root,
    text="Welcome to Tkinter Day 1",
    font=("Segoe UI", 16, "bold"),
    fg="white",
    bg="#1e1e1e",
)
title_label.pack(pady=20)

subtitle_label = tk.Label(
    root,
    text="Click a button to test events",
    font=("Segoe UI", 12),
    fg="#cccccc",
    bg="#1e1e1e",
)
subtitle_label.pack(pady=5)

def on_next_click():
    messagebox.showinfo("Next", "Tomorrow you will build inputs and layouts!")

def on_exit_click():
    root.destroy()  # closes the window

next_button = tk.Button(
    root,
    text="Next",
    font=("Segoe UI", 12),
    padx=10,
    pady=5,
    command=on_next_click,   # no parentheses here
)
next_button.pack(pady=10)

exit_button = tk.Button(
    root,
    text="Exit",
    font=("Segoe UI", 12),
    padx=10,
    pady=5,
    command=on_exit_click,
)
exit_button.pack(pady=5)

root.mainloop()

