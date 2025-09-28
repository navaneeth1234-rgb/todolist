tasks = []
def display_menu():
    print("1.add task")
    print("2.edit task")
    print("3.delete task")
    print("4.exit")

while True:
    display_menu()
    choice=input("select an option..")

    if choice =='1':
        task = input("enter the task..")
        tasks.append(task)
        print("task added successfully!")
    elif choice =='2':
        if tasks: #to check are there task awailable to  edit 
            for index, task in enumerate(tasks):  #display the current task with their indexes
                print(f"{index+1}.{task}")  
            try:
                task_index = int(input("enter the task index to edit"))
                if 0<=task_index<len(tasks):
                    new_task=input("enter a new task")
                    tasks[task_index]=new_task
                    print("task editted successfuly!")
                else:
                    print("Invalid index")
            except ValueError:
                print("please enter a valid number")
                
            else:
                print("no task awailable to  edit")
        elif choice=='3':
            if tasks:
                for index, task in enumerate(tasks):
                    print(f"{index+1}.{task}")
                try:
                    task_index = int(input("enter the task index"))
                    if 0<=task_index<len(tasks):
                        tasks.pop(task_index)
                        print("task deleted successfully!")
                    else:
                        print("invalid index")
                except ValueError:
                    print("please enter a valid number")
            else:
                print("no task available to delete")
        elif choice=='4':
            print("exiting...")
            break
        else:
            print("invalid choice. Enter a valid choice")
                            