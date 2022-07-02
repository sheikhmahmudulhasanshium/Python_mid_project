def check(task_list):
    if task_list:
        print(".....................Check Schedule Clashed......................\n")

        clashed_scedule_list=[]
        
        for i in range(len(task_list)):
            for j in range(len(task_list)):
                if i!=j:
                    if task_list[i]["time"]==task_list[j]["time"]:
                        clashed_scedule_list.append(task_list[i])
        print(clashed_scedule_list)
        # else: # end of list reached
        if clashed_scedule_list: #if empty list
            print("No clash found.")
        else:
            print(clashed_scedule_list)

    else:
        print("Can not search from empty task list.")
        