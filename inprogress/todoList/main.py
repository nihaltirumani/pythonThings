def get_tasks():
    global content
    with open("inprogress/todoList/data.txt", "r") as file:
        content = [task.strip() for task in file.readlines()]

def show_tasks():
        print("Tasks:")
        if content == []:
            print("No tasks.")
        else:
            for i in range(1, len(content) + 1):
                print(f"\t{i}. {content[i - 1]}")

def add_task(task):
    content.append(task)

def delete_task(index):
    content.pop(index - 1)

print("Welcome to TO-DO list.")

content = []
get_tasks()

while True:
    print("What would you like to do?")
    print(
"""\t1. Add a new task
\t2. View tasks
\t3. Remove a task
\t4. Exit""")
    
    try:
        user_choise = int(input("Enter your choice: "))
    except ValueError:
        quit()

    if user_choise == 1:
        user_task = input("Enter the task:\n")
        add_task(user_task)
    elif user_choise == 2:
        show_tasks()
    elif user_choise == 3:
        user_index = int(input("Enter the index of the task: "))
        delete_task(user_index)
    elif user_choise == 4:
        quit()
        with open("inprogress/todoList/data.txt", "w") as file:
            for i in range(len(content)):
                raw += f"{content[i]}\n"
            file.write(raw)