tasks = []
ch = "yes"

while ch.lower() == "yes":
    print("\n- TO DO LIST -")
    print("1. Add task")
    print("2. View list")
    print("3. Delete task")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task successfully inserted")

    elif choice == 2:
        if len(tasks) == 0:
            print("No task available")
        else:
            print("\nTasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == 3:
        if len(tasks) == 0:
            print("No task available")
        else:
            n = int(input("Enter task number to remove: "))
            if n <= len(tasks):
                tasks.pop(n - 1)
                print("Task has been removed")
            else:
                print("Invalid task number")

    elif choice == 4:
        print("EXITING...")
        break

    else:
        print("Invalid choice")

    ch = input("Do you want to continue (yes/no): ")
