import os
from datetime import datetime

def display_menu():
    print("\n===== Daily Planner Menu =====")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Add a Note")
    print("5. View Notes")
    print("6. Exit")
    print("==============================")

def add_task(task_file):
    task = input("Enter your task: ")
    deadline = input("Enter deadline (optional, e.g., 2024-12-31): ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(task_file, "a") as file:
        file.write(f"Task: {task}, Deadline: {deadline if deadline else 'No deadline'}, Added on: {timestamp}, Status: Pending\n")
    print("Task added successfully!")

def view_tasks(task_file):
    if not os.path.exists(task_file):
        print("No tasks found!")
        return
    print("\n===== Your Tasks =====")
    with open(task_file, "r") as file:
        tasks = file.readlines()
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")

def mark_task_done(task_file):
    if not os.path.exists(task_file):
        print("No tasks found!")
        return
    view_tasks(task_file)
    task_number = int(input("Enter the task number to mark as done: "))
    with open(task_file, "r") as file:
        tasks = file.readlines()
    if 0 < task_number <= len(tasks):
        task = tasks[task_number - 1]
        updated_task = task.replace("Status: Pending", "Status: Done")
        tasks[task_number - 1] = updated_task
        with open(task_file, "w") as file:
            file.writelines(tasks)
        print("Task marked as done!")
    else:
        print("Invalid task number.")

def add_note(note_file):
    note = input("Enter your note: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(note_file, "a") as file:
        file.write(f"Note: {note}, Added on: {timestamp}\n")
    print("Note added successfully!")

def view_notes(note_file):
    if not os.path.exists(note_file):
        print("No notes found!")
        return
    print("\n===== Your Notes =====")
    with open(note_file, "r") as file:
        notes = file.readlines()
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note.strip()}")

def main():
    task_file = "daily_tasks.txt"
    note_file = "daily_notes.txt"
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(task_file)
        elif choice == "2":
            view_tasks(task_file)
        elif choice == "3":
            mark_task_done(task_file)
        elif choice == "4":
            add_note(note_file)
        elif choice == "5":
            view_notes(note_file)
        elif choice == "6":
            print("Exiting... Have a productive day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
