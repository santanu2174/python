def app_task():
    tasks = []
    print("----WELCOME TO TASK MANAGEMENT SYSTEM----")

    total_task = int(input("Enter How many task added = "))

    for i in range(1, total_task+1):
        task_name = input(f"Enter {i} task:  ")
        tasks.append(task_name)
    print(f"Al of Tasks : \n{tasks} ")
    while True:
        Choice = int(input("Select 1-ADD\n2-UPDATE\n3-DELETE\n4-EXIT\n"))
        if Choice == 1:
            add = input("You added a task: ")
            tasks.append(add)
            print("Task added successfully!")
            print(f"All Tasks: {tasks}")
        elif Choice == 2:
            update_value = input("Enter the task name for update : ")
            if update_value in tasks:
                new_task = input("Enter new task name: ")
                up = tasks.index(update_value)
                tasks[up] = new_task
                print(f"Task update value is: {new_task}")
                print(f"All Tasks: {tasks}")
            else:
                print("Inavalid Task")
        elif Choice == 3:
            del_value = input("Enter Task name for Delete : ")
            if del_value in tasks:
                ind = tasks.index(del_value)
                del tasks[ind]
                print("Task Delete successfully!")
                print(f"All Tasks: {tasks}")
            else:
                print("Invalid task name")
        elif Choice == 4:
            print("Closing the Progammes")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    app_task()




