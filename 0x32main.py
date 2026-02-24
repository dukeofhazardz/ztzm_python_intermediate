import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


# ---------------- DECORATOR ---------------- #
def log_task(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[LOGGED] Task added at {timestamp}\n")
        return result
    return wrapper


# ---------------- TASK MANAGER CLASS ---------------- #
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.tasks, file, indent=4)

    @log_task
    def add_task(self):
        print("> Add Task")
        name = input("Name: ")
        priority = input("Priority: ")
        deadline = input("Deadline: ")

        task = {
            "name": name,
            "priority": priority,
            "deadline": deadline
        }

        self.tasks.append(task)
        self.save_tasks()

    def task_generator(self):
        # Sort tasks by deadline before yielding
        sorted_tasks = sorted(
            self.tasks,
            key=lambda x: datetime.strptime(x["deadline"], "%Y-%m-%d")
        )

        for task in sorted_tasks:
            yield task

    def next_task(self):
        print("> Next Tasks\n")
        for task in self.task_generator():
            print(f"{task['name']} | Priority: {task['priority']} | Deadline: {task['deadline']}")
        print()


# ---------------- MAIN PROGRAM ---------------- #
def main():
    manager = TaskManager()

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit\n")

        choice = input("Choose an option: ")

        if choice == "1":
            manager.add_task()
        elif choice == "2":
            manager.next_task()
        elif choice == "3":
            print("Exiting Task Scheduler.")
            break
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()