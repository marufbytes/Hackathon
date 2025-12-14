tasks = []

while True:
    print("\n TO DO LIST ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            num = int(input("Enter task number: "))
            if num > 0 and num <= len(tasks):
                removed = tasks.pop(num - 1)
                print("Removed:", removed)
            else:
                print("Invalid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
