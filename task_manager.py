import json, os
from datetime import datetime

TASK_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task():
    title = input("Title: ")
    desc = input("Description: ")
    due = input("Due Date (YYYY-MM-DD): ")
    task = {"title": title, "description": desc, "due": due, "status": "Pending"}
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!\n")

def view_tasks():
    tasks = load_tasks()
    for i, t in enumerate(sorted(tasks, key=lambda x: x['due'])):
        print(f"{i+1}. {t['title']} | {t['due']} | {t['status']}")
    print()

def mark_done():
    view_tasks()
    index = int(input("Enter task number to mark completed: ")) - 1
    tasks = load_tasks()
    tasks[index]['status'] = 'Completed'
    save_tasks(tasks)
    print("✅ Task marked as completed!\n")

def delete_task():
    view_tasks()
    index = int(input("Enter task number to delete: ")) - 1
    tasks = load_tasks()
    del tasks[index]
    save_tasks(tasks)
    print("🗑️ Task deleted!\n")

def menu():
    while True:
        print("====== 📋 Task Manager ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose: ")

        if choice == '1': add_task()
        elif choice == '2': view_tasks()
        elif choice == '3': mark_done()
        elif choice == '4': delete_task()
        elif choice == '5': break
        else: print("⚠️ Invalid choice")

if __name__ == "__main__":
    menu()
