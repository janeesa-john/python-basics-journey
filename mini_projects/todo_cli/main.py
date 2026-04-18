# CLI To-Do Application
# Allows users to add, view, and delete tasks using file handling

def add_task():
    task = input("Enter task: ")

    with open("tasks.txt", 'a') as file:
        file.write(task + "\n")

    print("Task added successfully")

def view_tasks():
    with open("tasks.txt", 'r') as file:
        tasks = file.readlines()

        if not tasks:
            print("No tasks found")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(i,'.',task.strip())

def delete_task():
    with open("tasks.txt", 'r') as file:
        tasks = file.readlines()

        if not tasks:
            print("No tasks to delete")
            return

        print("\nTasks:")
        for i, task in enumerate(tasks, start=1):
            print(i, '.', task.strip())

        num = int(input("Enter task number to delete: "))

        if 1 <= num <= len(tasks):
            tasks.pop(num-1)

            with open("tasks.txt", "w") as file:
                file.writelines(tasks)

                print("Task deleted successfully")
        else:
            print("Invalid task number")


print("\n===== TO-DO APP =====")

while True:
    print("\nTo-Do App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")