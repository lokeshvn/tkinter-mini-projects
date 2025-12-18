import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Day 4 – Temperature Converter (°C ↔ °F)")
root.geometry("420x230")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

# ----- Row 0: Celsius input -----
tk.Label(frame, text="Celsius (°C):").grid(row=0, column=0, padx=10, pady=5, sticky="e")

celsius_entry = tk.Entry(frame, width=15)
celsius_entry.grid(row=0, column=1, padx=10, pady=5)

# ----- Row 1: Fahrenheit input -----
tk.Label(frame, text="Fahrenheit (°F):").grid(row=1, column=0, padx=10, pady=5, sticky="e")

fahrenheit_entry = tk.Entry(frame, width=15)
fahrenheit_entry.grid(row=1, column=1, padx=10, pady=5)

# ----- Row 2: Buttons -----
def c_to_f():
    value = celsius_entry.get().strip()
    if not value:
        messagebox.showwarning("Input required", "Please enter a Celsius value.")
        return
    try:
        c = float(value)
    except ValueError:
        messagebox.showerror("Invalid input", "Celsius must be a number.")
        return

    f = (c * 9 / 5) + 32
    fahrenheit_entry.delete(0, tk.END)
    fahrenheit_entry.insert(0, f"{f:.2f}")
    result_label.config(text=f"{c:.2f} °C = {f:.2f} °F")


def f_to_c():
    value = fahrenheit_entry.get().strip()
    if not value:
        messagebox.showwarning("Input required", "Please enter a Fahrenheit value.")
        return
    try:
        f = float(value)
    except ValueError:
        messagebox.showerror("Invalid input", "Fahrenheit must be a number.")
        return

    c = (f - 32) * 5 / 9
    celsius_entry.delete(0, tk.END)
    celsius_entry.insert(0, f"{c:.2f}")
    result_label.config(text=f"{f:.2f} °F = {c:.2f} °C")


c_to_f_button = tk.Button(frame, text="°C → °F", width=10, command=c_to_f)
c_to_f_button.grid(row=2, column=0, padx=10, pady=10, sticky="e")

f_to_c_button = tk.Button(frame, text="°F → °C", width=10, command=f_to_c)
f_to_c_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# ----- Row 3: Result label -----
result_label = tk.Label(frame, text="", font=("Segoe UI", 11), fg="blue")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Enter key: default to Celsius → Fahrenheit
root.bind("<Return>", lambda event: c_to_f())

root.mainloop()
