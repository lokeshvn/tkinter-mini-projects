import tkinter as tk
from tkinter import messagebox

# ---------- LOGIN WINDOW ----------

root = tk.Tk()
root.title("Mini Project – Login")
root.geometry("400x260")

# center container
form_frame = tk.Frame(root, padx=20, pady=20)
form_frame.pack(expand=True)

# title label
title_label = tk.Label(
    form_frame,
    text="Developer Login",
    font=("Segoe UI", 16, "bold")
)
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 15))

# username + password
tk.Label(form_frame, text="Username:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(form_frame, text="Password:").grid(row=2, column=0, padx=10, pady=5, sticky="e")

username_entry = tk.Entry(form_frame, width=25)
username_entry.grid(row=1, column=1, padx=10, pady=5)

password_entry = tk.Entry(form_frame, width=25, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

status_label = tk.Label(form_frame, text="", fg="red")
status_label.grid(row=4, column=0, columnspan=2, pady=10)


def open_profile_window(username: str):
    """Open a new window that shows a simple profile."""
    profile = tk.Toplevel(root)
    profile.title("Developer Profile")
    profile.geometry("450x250")

    profile_frame = tk.Frame(profile, padx=20, pady=20)
    profile_frame.pack(expand=True, fill="both")

    tk.Label(
        profile_frame,
        text=f"Welcome, {username}",
        font=("Segoe UI", 16, "bold")
    ).pack(pady=(0, 10))

    tk.Label(
        profile_frame,
        text="Role: Associate Software Developer",
        font=("Segoe UI", 12)
    ).pack(pady=2)

    tk.Label(
        profile_frame,
        text="Focus: Python · Tkinter · Backend APIs",
        font=("Segoe UI", 11)
    ).pack(pady=2)

    tk.Label(
        profile_frame,
        text="Goal: Build clean, testable desktop tools to showcase skills.",
        font=("Segoe UI", 10),
        wraplength=380,
        justify="center"
    ).pack(pady=(10, 20))

    tk.Button(
        profile_frame,
        text="Logout (Close Profile)",
        command=profile.destroy
    ).pack(pady=5)


def validate_login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        status_label.config(text="Please enter username and password", fg="red")
        return

    # simple dummy check – replace with real logic later
    if username == "admin" and password == "admin123":
        status_label.config(text="Login successful!", fg="green")
        messagebox.showinfo("Login", "Welcome, login successful!")
        open_profile_window(username)
    else:
        status_label.config(text="Invalid credentials", fg="red")


login_button = tk.Button(form_frame, text="Login", width=15, command=validate_login)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

# allow Enter key to trigger login
root.bind("<Return>", lambda event: validate_login())

root.mainloop()
