# Simple To-Do List Application in Python   
# This application allows users to add, view, mark as completed, and remove tasks.


tasks = []


def show_menu():
    print("To-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

def add_task(task_name):
    if task_name:
        tasks.append({"name": task_name, "done": False})
        print(f"Task '{task_name}' added successfully.")
    else:
        print("Task name cannot be empty.")

def view_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['name']}")
    else:
        print("No tasks available.")

def mark_task_completed():
    num = int(input("Enter task number to mark as done: "))
    if 0 < num <= len(tasks):
        tasks[num - 1]["done"] = True
        print("Task marked as done.")
    else:
        print("Invalid task number.")

def remove_task():
    num = int(input("Enter task number to remove: "))
    if 0 < num <= len(tasks):
        tasks.pop(num - 1)
        print("Task removed successfully.")
    else:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task_name = input("Enter the task name: ")
        add_task(task_name)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_completed()
    elif choice == "4":
        remove_task()
    elif choice == "5": 
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please try again.")

