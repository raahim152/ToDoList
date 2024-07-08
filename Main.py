import tkinter as tk
from tkinter import simpledialog, messagebox

class Task:
    def __init__(self, taskID, taskName):
        self.taskID = taskID
        self.taskName = taskName
        self.completed = False

    def markCompleted(self):
        self.completed = True
    
    def __str__(self):
        status = 'Completed' if self.completed else 'Incomplete'
        return f'Task [{self.taskID}]: {self.taskName} - {status}'

class UserData:
    def __init__(self, id, name):
        self.id = id
        self.name = name
      
    def __str__(self):
        return f'User: [{self.id}]: {self.name}'

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("500x500")

        self.user_data_list = []
        self.task_list = []

        self.create_widgets()

    def create_widgets(self):
        self.user_id_label = tk.Label(self.root, text="User ID:")
        self.user_id_label.pack()
        self.user_id_entry = tk.Entry(self.root)
        self.user_id_entry.pack()

        self.user_name_label = tk.Label(self.root, text="User Name:")
        self.user_name_label.pack()
        self.user_name_entry = tk.Entry(self.root)
        self.user_name_entry.pack()

        self.user_button = tk.Button(self.root, text="Enter User", command=self.enter_user)
        self.user_button.pack()

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task_window)
        self.add_task_button.pack()

        self.mark_task_button = tk.Button(self.root, text="Mark Task", command=self.mark_task_window)
        self.mark_task_button.pack()

        self.remove_task_button = tk.Button(self.root, text="Remove Task", command=self.remove_task_window)
        self.remove_task_button.pack()

        self.show_tasks_button = tk.Button(self.root, text="Show Tasks", command=self.show_tasks)
        self.show_tasks_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack()

    def enter_user(self):
        user_id = self.user_id_entry.get()
        user_name = self.user_name_entry.get()

        if user_id and user_name:
            user_data = UserData(int(user_id), user_name)
            self.user_data_list.append(user_data)
            messagebox.showinfo("Info", "User entered successfully!")
        else:
            messagebox.showerror("Error", "Please enter both user ID and name.")

    def add_task_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Add Task")
        new_window.geometry("300x200")

        task_id_label = tk.Label(new_window, text="Task ID:")
        task_id_label.pack()
        task_id_entry = tk.Entry(new_window)
        task_id_entry.pack()

        task_name_label = tk.Label(new_window, text="Task Name:")
        task_name_label.pack()
        task_name_entry = tk.Entry(new_window)
        task_name_entry.pack()

        add_button = tk.Button(new_window, text="Add Task", command=lambda: self.add_task(task_id_entry.get(), task_name_entry.get(), new_window))
        add_button.pack()

    def add_task(self, task_id, task_name, window):
        if task_id and task_name:
            task1 = Task(int(task_id), task_name)
            self.task_list.append(task1)
            messagebox.showinfo("Info", f"Task {task1} added successfully!")
            window.destroy()
        else:
            messagebox.showerror("Error", "Please enter both task ID and name.")

    def mark_task_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Mark Task")
        new_window.geometry("300x200")

        task_id_label = tk.Label(new_window, text="Task ID:")
        task_id_label.pack()
        task_id_entry = tk.Entry(new_window)
        task_id_entry.pack()

        mark_button = tk.Button(new_window, text="Mark Task", command=lambda: self.mark_task(int(task_id_entry.get()), new_window))
        mark_button.pack()

    def mark_task(self, task_id, window):
        if task_id and 1 <= task_id <= len(self.task_list):
            self.task_list[task_id - 1].markCompleted()
            messagebox.showinfo("Info", f"Task {task_id} marked as completed!")
            window.destroy()
        else:
            messagebox.showerror("Error", "Invalid Task ID.")

    def remove_task_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Remove Task")
        new_window.geometry("300x200")

        task_id_label = tk.Label(new_window, text="Task ID:")
        task_id_label.pack()
        task_id_entry = tk.Entry(new_window)
        task_id_entry.pack()

        remove_button = tk.Button(new_window, text="Remove Task", command=lambda: self.remove_task(int(task_id_entry.get()), new_window))
        remove_button.pack()

    def remove_task(self, task_id, window):
        if task_id and 1 <= task_id <= len(self.task_list):
            self.task_list.pop(task_id - 1)
            messagebox.showinfo("Info", f"Task {task_id} removed successfully!")
            window.destroy()
        else:
            messagebox.showerror("Error", "Invalid Task ID.")

    def show_tasks(self):
        tasks = "\n".join(str(task) for task in self.task_list)
        users = "\n".join(str(user) for user in self.user_data_list)
        messagebox.showinfo("Tasks", f"Users:\n{users}\n\nTasks:\n{tasks}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
