import os

# File where tasks will be stored
FILE_PATH = "G:\internshiptechwithwarriors\Task4.txt"

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(FILE_PATH):
        return []
    
    with open(FILE_PATH, "r") as file:
        tasks = file.read().splitlines()
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(FILE_PATH, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")

def remove_task(task):
    """Remove a task."""
    tasks = load_tasks()
    if task in tasks:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Task removed: {task}")
    else:
        print(f"Task not found: {task}")

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if tasks:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")

def main():
    """Main loop for the command-line interface."""
    while True:
        print("\nTo-Do List Application")
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
