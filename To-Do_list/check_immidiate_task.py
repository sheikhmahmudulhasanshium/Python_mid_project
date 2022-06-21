def check(task_list):
    if task_list:
            print("Upcoming immidiate task/s:\n")

            upcoming = min(item['time'] for item in task_list)
            for i,item in enumerate(task_list):
                if item['time']==upcoming:
                    print(task_list[i])
    else:
        print("Can not search from empty task list.")