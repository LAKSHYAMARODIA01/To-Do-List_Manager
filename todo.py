import os

TASKS_FILE = 'tasks.txt'

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            for line in file:
                task_id, description, deadline, status = line.strip().split(', ')
                tasks.append({
                    'id': int(task_id),
                    'description': description,
                    'deadline': deadline,
                    'status': status
                })
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task['id']}, {task['description']}, {task['deadline']}, {task['status']}\n")

def add_task(tasks):
    description = input("Enter task description: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    task_id = len(tasks) + 1
    tasks.append({'id': task_id, 'description': description, 'deadline': deadline, 'status': 'Pending'})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    print("To-Do List:")
    pending_tasks = [task for task in tasks if task['status'] == 'Pending']
    completed_tasks = [task for task in tasks if task['status'] == 'Completed']

    if pending_tasks:
        print("[Pending]")
        for task in pending_tasks:
            print(f"{task['id']}. {task['description']} - Deadline: {task['deadline']}")
    else:
        print("[Pending] No tasks pending.")

    if completed_tasks:
        print("[Completed]")
        for task in completed_tasks:
            print(f"{task['id']}. {task['description']} - Deadline: {task['deadline']}")
    else:
        print("[Completed] No tasks completed yet.")

def edit_task(tasks):
    view_tasks(tasks)
    task_id = int(input("Enter task number to edit: "))
    for task in tasks:
        if task['id'] == task_id:
            new_description = input("Enter new description: ")
            new_deadline = input("Enter new deadline (YYYY-MM-DD): ")
            task['description'] = new_description
            task['deadline'] = new_deadline
            save_tasks(tasks)
            print("Task updated successfully!")
            return
    print("Task not found.")

def delete_task(tasks):
    view_tasks(tasks)
    task_id = int(input("Enter task number to delete: "))
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!")
            return
    print("Task not found.")

def mark_task_completed(tasks):
    view_tasks(tasks)
    task_id = int(input("Enter task number to mark as completed: "))
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Completed'
            save_tasks(tasks)
            print("Task marked as completed!")
            return
    print("Task not found.")

def main():
    tasks = load_tasks()
    while True:
        print("\nWelcome to To-Do List Manager!")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            mark_task_completed(tasks)
        elif choice == '6':
            print("Exiting the To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()