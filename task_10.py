class ToDoList:
    def __init__(self):
        self.tasks = []  # List to store tasks

    def add_task(self, name, description):
        """Add a new task to the list."""
        task = {"name": name, "description": description, "completed": False}
        self.tasks.append(task)
        print(f"Task '{name}' added successfully!")

    def mark_complete(self, task_name):
        """Mark a task as complete."""
        for task in self.tasks:
            if task["name"].lower() == task_name.lower():
                task["completed"] = True
                print(f"Task '{task_name}' marked as complete!")
                return
        print(f"Task '{task_name}' not found!")

    def display_tasks(self):
        """Display all tasks (completed & incomplete)."""
        if not self.tasks:
            print("No tasks available.")
            return

        print("\nTo-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            status = "✔ Done" if task["completed"] else "❌ Not Done"
            print(f"{index}. {task['name']} - {task['description']} [{status}]")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. Display Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            todo_list.add_task(name, description)

        elif choice == "2":
            task_name = input("Enter task name to mark as complete: ")
            todo_list.mark_complete(task_name)

        elif choice == "3":
            todo_list.display_tasks()

        elif choice == "4":
            print("Exiting To-Do List. Have a great day!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
