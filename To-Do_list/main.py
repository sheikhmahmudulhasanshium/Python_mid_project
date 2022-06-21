import add_task,update_task,delete_task,check_immidiate_task,display_task,conflict_task,store_task

#Empty list
task_list=[]

print("..........................tasks.............................")
while True:
    
    promt=("..........................Menu.................................")
    promt +=("\n Welcome user.")
    promt +=("\n Enter '+' to add task")
    promt +=("\n Enter '-' to delete task")
    promt +=("\n Enter 'x' to update task")
    promt +=("\n Enter '?' to search immidiate task")
    promt +=("\n Enter '!' to search conflicting task")
    promt +=("\n Enter '.' to show task list")
    promt +=("\n Enter 's' to store the current to do list")
    promt +=("\n Enter 'quit' to quit the system\n")
    user_input=input(promt)
    if user_input=='+':
        add_task.add(task_list)
        
    elif user_input=='x':
        update_task.update(task_list)
    elif user_input=="-":
        delete_task.delete(task_list)
    elif user_input=="?":
            print("....................Search Immidiate task/s..........................")
            check_immidiate_task.check(task_list)
    elif user_input=="!":
            conflict_task.check(task_list)
    
    elif user_input==".":
        display_task.display(task_list)
    elif user_input=="s":
        store_task.write(task_list)
        store_task.read(task_list)
    elif user_input=="quit":   
        break
    else:
        print("Enter correct option.")
