import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do list")
        self.root.geometry("400x500")
        self.root.config(bg="#F9F9F9")
        self.tasks = []

        self.title_label = tk.Label(root, text="Your To-Do list", font=("Helvetica", 16, "bold"), bg="#F9F9F9")
        self.title_label.pack(pady=10)

        self.task_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Tasks", command=self.add_tasks, bg="#A6E3E9")
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=40, height=15, font=("Helvetica", 12))
        self.task_listbox.pack(pady=10)

        self.done_button = tk.Button(root, text="Mark as Done", command=self.mark_done, bg="#B5F7B0")
        self.done_button.pack(pady=5)
        
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="#FFABAB")
        self.delete_button.pack(pady=5)

    def add_tasks(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_list()
        else:
            messagebox.showwarning("Selection Error", "No task selected!")

    def mark_done(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            if not task.startswith("✅ "):
                self.tasks[selected_task_index[0]] = f"✅ {task}"
            self.update_task_list()
        else:
            messagebox.showwarning("Selection Error", "No task completed!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
