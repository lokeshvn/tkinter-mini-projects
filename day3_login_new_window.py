import tkinter as tk

root = tk.Tk()
root.title("Login")
root.geometry("400x250")

form = tk.Frame(root, padx=20, pady=20)
form.pack(expand=True)

tk.Label(form, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(form, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")

username_entry = tk.Entry(form, width=25)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_entry = tk.Entry(form, width=25, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

status_label = tk.Label(form, text="", fg="red")
status_label.grid(row=3, column=0, columnspan=2, pady=10)

def open_main_window():
    main_win = tk.Toplevel(root)       # new window
    main_win.title("Main App")
    main_win.geometry("500x300")
    tk.Label(main_win, text="Welcome to the main app!").pack(pady=20)

def login():
    user = username_entry.get()
    pwd = password_entry.get()
    if user == "user1" and pwd == "abcd123":
        status_label.config(text="Login successful!", fg="green")
        open_main_window()
    else:
        status_label.config(text="Invalid username or password", fg="red")

login_button = tk.Button(form, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)
"""
root.mainloop()

Toplevel(root) creates an extra top-level window you can treat like a new screen.​

Login window stays visible; you can later hide it with root.withdraw() if desired  """
