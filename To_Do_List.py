tasks = []

def show_tasks():
    if not tasks:
        print("No tasks to show")
    else:
        print("Your tasks: ")
        for i, task in enumerate(tasks,1):
            print(f"{i}.{task['task']}-{'Done' if task['done'] else 'Not Done'}")
    
def add_task():
    task_name = input("Enter a new task: ")
    tasks.append({'task': task_name, 'done': False})

def mark_done():
    show_tasks()
    task_num =int(input("Enter Task number to mark as done: "))
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]['done'] = True
    else:
        print("Invalid task number.")