import os

DATA_FILE="tasks.txt"

def ensure_file():
    if not os.path.exists(DATA_FILE):
        open(DATA_FILE, "w").close()


def show_tasks():
    ensure_file()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        tasks = f.readlines()
        if not tasks:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, task.strip())

def add_task(task):
    ensure_file()
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(task + "\n")
    print("Task added!")

def delete_task(num):
    ensure_file()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        tasks = f.readlines()
    if 0 < num <= len(tasks):
        tasks.pop(num-1)    
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.writelines(tasks)
        print("Task deleted!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter Task: ")
            add_task(task)
        elif choice == "3":
            try:
                num = int(input("Enter task number top delete: "))
            except ValueError:
                print("Please enter a valid number.")
            delete_task(num)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid INPUT!!")

if __name__ == "__main__":
    main()

