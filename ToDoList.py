import tkinter as tk

class SimpleTodoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_widgets()
    
    def create_widgets(self):
        # Listbox to display tasks
        self.tasks = tk.Listbox(self, width=40, height=20)
        self.tasks.pack(pady=15)

        # Entry field for new tasks
        self.task_entry = tk.Entry(self, width=25)
        self.task_entry.pack(pady=5)

        # Button to add a new task
        self.add_button = tk.Button(self, text="Add Task", command=self.add_task, bg="green", fg="white")
        self.add_button.pack(pady=5)

        # Button to delete the selected task
        self.delete_button = tk.Button(self, text="Delete Task", command=self.remove_task, bg="red", fg="white")
        self.delete_button.pack(pady=5)

    def add_task(self):
        new_task = self.task_entry.get()
        if new_task:
            self.tasks.insert(tk.END, new_task)
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_task_index = self.tasks.curselection()
        if selected_task_index:
            self.tasks.delete(selected_task_index)

if __name__ == "__main__":
    app = SimpleTodoApp()
    app.mainloop()
