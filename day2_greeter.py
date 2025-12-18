import tkinter as tk

root = tk.Tk()
root.title("Day 2 – Greeter")
root.geometry("420x220")

tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Favorite language:").grid(row=1, column=0, padx=10, pady=5, sticky="e")

name_entry = tk.Entry(root, width=25)
name_entry.grid(row=0, column=1, padx=10, pady=5)

lang_entry = tk.Entry(root, width=25)
lang_entry.grid(row=1, column=1, padx=10, pady=5)

# output label (initially empty)
output_label = tk.Label(root, text="", fg="blue")
output_label.grid(row=3, column=0, columnspan=2, pady=10)

#pop up message
from tkinter import messagebox

def greet():
    name = name_entry.get()
    lang = lang_entry.get()
    messagebox.showinfo("Greeting", f"Hello {name}, nice to see a {lang} developer here!")

#inlinee message
    
##def greet():
##    name = name_entry.get()
##    lang = lang_entry.get()
##    message = f"Hello {name}, nice to see a {lang} developer here!"
##    output_label.config(text=message)

def greet_event(event=None):
    greet()  # or put greet logic here directly

root.bind("<Return>", greet_event)

#Binding <Return> on the root window calls your function
#when Enter is pressed while the window is focused

greet_button = tk.Button(root, text="Greet me", command=greet)
greet_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
