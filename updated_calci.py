import tkinter as tk

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator – Tkinter")
        self.geometry("320x420")
        self.resizable(False, False)
        self.configure(bg="#1e1e1e")

        self.current_expression = ""

        self._build_ui()

    def _build_ui(self):
        display_frame = tk.Frame(self, bg="#1e1e1e")
        display_frame.pack(fill="x", padx=10, pady=10)

        self.display = tk.Entry(
            display_frame,
            font=("Segoe UI", 18),
            justify="right",
            bd=0,
            relief="flat",
            bg="#2d2d2d",
            fg="#ffffff",
            insertbackground="#ffffff"
        )
        self.display.pack(fill="x", ipady=10)

        buttons_frame = tk.Frame(self, bg="#1e1e1e")
        buttons_frame.pack(padx=10, pady=10)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
        ]

        for (text, r, c) in buttons:
            if text == "C":
                cmd = self.clear_display
                bg = "#ff5555"
            elif text in {"/", "*", "-", "+"}:
                cmd = lambda v=text: self.update_display(v)
                bg = "#3b3b3b"
            else:
                cmd = lambda v=text: self.update_display(v)
                bg = "#262626"

            btn = tk.Button(
                buttons_frame,
                text=text,
                width=5,
                height=2,
                font=("Segoe UI", 12),
                bg=bg,
                fg="#ffffff",
                activebackground="#505050",
                activeforeground="#ffffff",
                relief="flat",
                command=cmd
            )
            btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)

        equals_button = tk.Button(
            buttons_frame,
            text="=",
            font=("Segoe UI", 12, "bold"),
            bg="#0078d4",
            fg="#ffffff",
            activebackground="#0a84ff",
            activeforeground="#ffffff",
            relief="flat",
            height=2,
            command=self.calculate_result
        )
        equals_button.grid(row=5, column=0, columnspan=4, padx=5, pady=(10, 0), sticky="nsew")

        self.bind("<Return>", lambda event: self.calculate_result())

    def update_display(self, value):
        self.current_expression += str(value)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_expression)

    def clear_display(self):
        self.current_expression = ""
        self.display.delete(0, tk.END)

    def calculate_result(self):
        if not self.current_expression:
            return
        try:
            result = eval(self.current_expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.current_expression = str(result)
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.current_expression = ""


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
