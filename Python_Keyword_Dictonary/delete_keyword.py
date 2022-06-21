import search_keyword
def delete(list):
    print("....................Delete Keyword..........................")
    required_key_name=input("Enter keyword name:")
    flag=search_keyword.search_list(list,required_key_name)
    if flag==True:
        for i,item in enumerate(list):
            if item["name"]==required_key_name:
                del list[i]
        else: #end of list reached
            print("deleted")
            print(f"current keywords: \n{list}")