# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Function to add a task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

# Function to delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter task number to delete: "))
        if 0 < task_number <= len(tasks):
            task = tasks.pop(task_number - 1)
            print(f"Task '{task}' deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program to drive the app
def main():
    tasks = []  # List to hold tasks

    while True:
        print("\n1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
