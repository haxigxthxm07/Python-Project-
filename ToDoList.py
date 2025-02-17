import json

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task_name):
        self.tasks.append({"task": task_name, "completed": False})
        self.save_tasks()

    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. {task['task']} [{status}]")

    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            self.save_tasks()
        else:
            print("Invalid task number!")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
            self.save_tasks()
        else:
            print("Invalid task number!")

if __name__ == "__main__":
    todo = ToDoList()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task Complete\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task_name = input("Enter task name: ")
            todo.add_task(task_name)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to mark complete: ")) - 1
            todo.mark_task_complete(task_number)
        elif choice == "4":
            task_number = int(input("Enter task number to delete: ")) - 1
            todo.delete_task(task_number)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")
