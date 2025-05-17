from datetime import datetime

# Base class
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def is_overdue(self):
        return not self.completed and datetime.now() > self.due_date

    def __str__(self):
        status = "✔️ Completed" if self.completed else "❌ Pending"
        return f"{self.title} - {status} | Due: {self.due_date.date()}"

# Inherited class for priority tasks
class PriorityTask(Task):
    def __init__(self, title, description, due_date, priority):
        super().__init__(title, description, due_date)
        self.priority = priority  # High, Medium, Low

    def __str__(self):
        base = super().__str__()
        return f"{base} | Priority: {self.priority}"

# Manager class that encapsulates task operations
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def show_all_tasks(self):
        if not self.tasks:
            print("📭 No tasks available.")
            return
        for task in self.tasks:
            print(task)

    def show_overdue_tasks(self):
        overdue = [task for task in self.tasks if task.is_overdue()]
        if not overdue:
            print("🎉 No overdue tasks.")
        else:
            print("⏰ Overdue Tasks:")
            for task in overdue:
                print(task)

    def mark_task_done(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                print(f"✅ Task '{title}' marked as completed.")
                return
        print(f"❌ Task '{title}' not found.")

# Application class (abstraction layer)
class TaskApp:
    def __init__(self):
        self.manager = TaskManager()

    def run(self):
        print("📝 Welcome to Task Manager App 📝")
        while True:
            print("\n1. Add Task")
            print("2. Add Priority Task")
            print("3. View All Tasks")
            print("4. View Overdue Tasks")
            print("5. Mark Task as Done")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.add_priority_task()
            elif choice == "3":
                self.manager.show_all_tasks()
            elif choice == "4":
                self.manager.show_overdue_tasks()
            elif choice == "5":
                title = input("Enter task title to mark done: ")
                self.manager.mark_task_done(title)
            elif choice == "6":
                print("👋 Goodbye!")
                break
            else:
                print("❗ Invalid choice. Try again.")

    def add_task(self):
        title = input("Title: ")
        description = input("Description: ")
        due_date = input("Due date (YYYY-MM-DD): ")
        task = Task(title, description, due_date)
        self.manager.add_task(task)
        print("✅ Task added.")

    def add_priority_task(self):
        title = input("Title: ")
        description = input("Description: ")
        due_date = input("Due date (YYYY-MM-DD): ")
        priority = input("Priority (High/Medium/Low): ")
        task = PriorityTask(title, description, due_date, priority)
        self.manager.add_task(task)
        print("✅ Priority task added.")

# Run the app
if __name__ == "__main__":
    app = TaskApp()
    app.run()
# This code implements a simple task manager application with the ability to add tasks, mark them as complete, and view overdue tasks.
# It uses object-oriented programming principles to create a base Task class and an inherited PriorityTask class.
# The TaskManager class manages the
#tasks, while the TaskApp class provides a user interface for interaction.
# The application allows users to add tasks, view all tasks, view overdue tasks, and mark tasks as done.