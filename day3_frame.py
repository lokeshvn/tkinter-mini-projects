##import tkinter as tk
##
##root = tk.Tk()
##root.title("Day 3 – Frames & Layout")
##root.geometry("400x250")
##
### outer frame, centered with pack
##form_frame = tk.Frame(root, padx=20, pady=20)
##form_frame.pack(expand=True)
##
##root.mainloop()

import tkinter as tk

root = tk.Tk()
root.title("Day 3 – Login Layout")
root.geometry("400x250")

form_frame = tk.Frame(root, padx=20, pady=20)
form_frame.pack(expand=True)

tk.Label(form_frame, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(form_frame, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")

username_entry = tk.Entry(form_frame, width=25)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_entry = tk.Entry(form_frame, width=25, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

status_label = tk.Label(form_frame, text="", fg="red")
status_label.grid(row=3, column=0, columnspan=2, pady=10)

def login():
    user = username_entry.get()
    pwd = password_entry.get()
    if user == "user1" and pwd == "abcd123":
        status_label.config(text="Login successful!", fg="green")
    else:
        status_label.config(text="Invalid username or password", fg="red")

login_button = tk.Button(form_frame, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
