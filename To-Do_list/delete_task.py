import add_task
def delete_task(task_list,task_description):
    confirmation_message=input("Do you want to delete the task? Y/N: ")
    if confirmation_message=="Y" or confirmation_message=="y":
           
        for index,item in enumerate(task_list):
                if item["description"]==task_description:
                    
                    del task_list[index]
            
        print(f"Current task List:\n{task_list}")
        print("task deleted.")
    else:
        print("Cancelled.")
def delete(task_list):
    if task_list:
            print("....................Delete task..........................")
            print(f"Previous task List:\n{task_list}")
            task_description=input("Enter description to delete:")
            for index,item in enumerate(task_list):
                if item["description"]==task_description:
        
                    delete_task(task_list,task_description)
                    break
            else:
                print("task not found.")
                user_input=input("Do you want to add new task?(y/n)")
                if(user_input=='y' or user_input=='Y'):
                    add_task.add(task_list)
                else:
                    print("Cancelled")
    else:
            print("Can not delete from empty task list.")
        