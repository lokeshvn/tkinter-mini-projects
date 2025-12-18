import tkinter as tk
from tkinter import messagebox


class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("To-Do List – Tkinter OOP")
        self.geometry("400x400")
        self.resizable(False, False)

        # internal state: simple list of strings (tasks)
        self.tasks: list[str] = []

        self._build_ui()

    def _build_ui(self):
        # ----- top: title -----
        title_label = tk.Label(
            self,
            text="My To-Do List",
            font=("Segoe UI", 16, "bold")
        )
        title_label.pack(pady=(10, 5))

        # ----- middle: listbox + scrollbar -----
        list_frame = tk.Frame(self)
        list_frame.pack(fill="both", expand=True, padx=15, pady=5)

        self.listbox = tk.Listbox(
            list_frame,
            height=10,
            font=("Segoe UI", 11),
            selectmode=tk.SINGLE
        )
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # ----- bottom: entry + buttons -----
        entry_frame = tk.Frame(self)
        entry_frame.pack(fill="x", padx=15, pady=(5, 10))

        self.task_var = tk.StringVar()

        task_entry = tk.Entry(
            entry_frame,
            textvariable=self.task_var,
            font=("Segoe UI", 11)
        )
        task_entry.grid(row=0, column=0, columnspan=2, sticky="ew", padx=(0, 5), pady=5)
        entry_frame.columnconfigure(0, weight=1)

        add_button = tk.Button(
            entry_frame,
            text="Add",
            width=8,
            command=self.add_task
        )
        add_button.grid(row=0, column=2, padx=(0, 5), pady=5)

        delete_button = tk.Button(
            entry_frame,
            text="Delete",
            width=8,
            command=self.delete_selected_task
        )
        delete_button.grid(row=1, column=2, padx=(0, 5), pady=5)

        clear_button = tk.Button(
            entry_frame,
            text="Clear All",
            width=8,
            command=self.clear_all_tasks
        )
        clear_button.grid(row=1, column=1, sticky="e", pady=5, padx=(5, 0))

        # Enter key adds task
        self.bind("<Return>", lambda event: self.add_task())

    # ----- behavior methods -----
    def add_task(self):
        text = self.task_var.get().strip()
        if not text:
            messagebox.showwarning("Empty task", "Please type a task before adding.")
            return

        self.tasks.append(text)
        self.listbox.insert(tk.END, text)
        self.task_var.set("")

    def delete_selected_task(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showinfo("No selection", "Please select a task to delete.")
            return

        index = selection[0]
        self.listbox.delete(index)
        del self.tasks[index]

    def clear_all_tasks(self):
        if not self.tasks:
            return
        if messagebox.askyesno("Clear all", "Are you sure you want to delete all tasks?"):
            self.listbox.delete(0, tk.END)
            self.tasks.clear()


if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
