from datetime import datetime
import add_task
def update_task(task_list,required_description,task_location,task_time):
    for index,item in enumerate(task_list):
        if(item["description"]==required_description):
            item["description"]=required_description
            item["location"]=task_location
            item["time"]=task_time
            task_list[index]=item
def update(task_list):
        print("....................Update task..........................")        
        
        print("................Update task Information...............")
        required_description=input("Enter description to add task :")
        for index,item in enumerate(task_list):
            if(item["description"]==required_description):
    
                task_location=input("Enter location:")
                try:
                    task_time_string=str(input("Enter New Time in (yyyy-mm-dd hh:mm) format:"))
                    task_time=datetime.strptime(task_time_string, "%Y-%m-%d %H:%M")
                except:
                    print("Follow the datetime format carefully")

                update_task(task_list,required_description,task_location,task_time)
                print("Task updated.")
                break
        else:
            print("Task not found")
            user_input=input("Do you want to add new task?(y/n)")
            if(user_input=='y' or user_input=='Y'):
                add_task.add(task_list)
            else:
                print("Cancelled")