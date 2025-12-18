import tkinter as tk

root = tk.Tk()
root.title("Day 2 – Entry Basics")
root.geometry("400x200")

name_label = tk.Label(root, text="Your name:")
name_label.pack(pady=5)

name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

def say_hello():
    name = name_entry.get()  # read text from Entry
    print(f"Hello, {name}!")

hello_button = tk.Button(root, text="Say Hello", command=say_hello)
hello_button.pack(pady=10)

root.mainloop()
