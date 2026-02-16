def task():
    tasks = [] #empty List
    print("-----WELCOME TO THE MANAGEMENT APP----")

    total_task = int(input("Enter how many task you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
    print(f"Today's tasks are\n{tasks}")
    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-Exit\n"))
        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print("Task added successfully")
            print(f"Today's tasks are\n{tasks}")
        elif operation == 2:
            update_value = input("Enter task name you want to update = ")
            if update_value in tasks:
                up = input("Enter new task name = ")
                ind = tasks.index(update_value)
                tasks[ind] = up
                print(f"Updated Task {up}")
                print(f"Today's tasks are\n{tasks}")
            else:
                print("Task not found")
        elif operation == 3:
            del_val = input("Enter task name you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Message {del_val} has been deleted")
            else:
                print("Task not found")
        elif operation == 4:
            print("Closing the program....")
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    task()
