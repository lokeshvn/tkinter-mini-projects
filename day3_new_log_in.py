
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

def login():
    user = username_entry.get()
    pwd = password_entry.get()
    if user == "user1" and pwd == "abcd123":
        root.destroy()        # close login window completely[web:158]
        open_main_root()      # create a new root window

def open_main_root():
    main_root = tk.Tk()
    main_root.title("Main App")
    main_root.geometry("500x300")
    tk.Label(main_root, text="Main app here").pack(pady=20)
    main_root.mainloop()


login_button = tk.Button(form, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

