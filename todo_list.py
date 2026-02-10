import os

FILE_NAME = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                title, status = line.strip().split("||")
                tasks.append({"title": title, "done": status == "1"})
    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            status = "1" if task["done"] else "0"
            file.write(f"{task['title']}||{status}\n")


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\nYour To-Do List:")
    for index, task in enumerate(tasks, start=1):
        mark = "✔" if task["done"] else "✗"
        print(f"{index}. [{mark}] {task['title']}")
    print()


def add_task(tasks):
    title = input("Enter task description: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("Task added successfully.\n")
    else:
        print("Task cannot be empty.\n")


def update_task(tasks):
    show_tasks(tasks)
    try:
        choice = int(input("Select task number to update: "))
        if 1 <= choice <= len(tasks):
            new_title = input("Enter new description: ").strip()
            if new_title:
                tasks[choice - 1]["title"] = new_title
                save_tasks(tasks)
                print("Task updated.\n")
            else:
                print("Update cancelled.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def mark_complete(tasks):
    show_tasks(tasks)
    try:
        choice = int(input("Select task number to mark complete: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as completed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        choice = int(input("Select task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed['title']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    tasks = load_tasks()

    while True:
        print("---- TO-DO LIST MENU ----")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Mark task as completed")
        print("5. Delete task")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_complete(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye! Stay productive 🚀")
            break
        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()
