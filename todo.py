def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Mark Task as Complete")
    print("4. Remove a Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            status = "✔" if task['completed'] else "✘"
            print(f"{idx}. {task['title']} [{status}]")

def add_task(tasks):
    task_title = input("Enter the task: ")
    tasks.append({"title": task_title, "completed": False})
    print(f"Task '{task_title}' added successfully!")

def mark_task_complete(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the task number to mark as complete: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]['completed'] = True
                print(f"Task '{tasks[task_number - 1]['title']}' marked as complete!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task['title']}' removed successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Exiting the To-Do List. Bye Bye! Have a Good Day:)")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
