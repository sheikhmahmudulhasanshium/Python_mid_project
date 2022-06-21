from datetime import datetime
def add_new(task_list,task_description,task_location,task_time):
    task={"description":task_description,"location":task_location,"time":task_time}
    confirmation_message=input("Do you want to save the task? Y/N: ")
    if confirmation_message=="Y" or confirmation_message=="y":
        task_list.append(task)
        print(task_list)
        print("Task added.")
    else:
        print("Cancelled.")

def add(task_list):
            print("....................Add New task..........................")
            task_description=input("Enter task description:")
            task_location=input("Enter location:")
            try:
                task_time_string=str(input("Enter  time in (yyyy-mm-dd hh:mm) format: "))
                task_time=str(datetime.strptime(task_time_string, "%Y-%m-%d %H:%M"))
                add_new(task_list,task_description,task_location,task_time)
            except ValueError:
                print("Follow the datetime format carefully")
            
            