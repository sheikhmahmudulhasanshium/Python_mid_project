import add_keyword
def search_list(key_list,required_keyword):
    for i,item in enumerate(key_list):
            if(item["name"]==required_keyword):
                print("Keyword Found")
                print(key_list[i]) 
                return True #if searched result exists, can update/delete
                break

    else:#end of list reached
        print("No such a key found")
        is_from_search=True
        add_keyword.add_keyword(key_list,is_from_search) 
def search(list):
        if list:
            print("....................Search Keyword..........................")
            u_input=input("Enter Keyword Name to Search: ")
            search_list(list,u_input)
        else:
            print("Can not search from empty contact list.")
            