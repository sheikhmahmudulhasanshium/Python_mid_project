import search_keyword,add_keyword
def update_keyword(list):
    print("....................Update Keyword..........................")
    required_keyword=input("Enter keyword to search:")       
    flag=search_keyword.search_list(list,required_keyword)
    if flag==True:
        new_name=input("Enter new keyword name to update:")
        new_details=input("Enter new keyword details to update:")
        new_sample=input("Enter new keyword sample code to update:")
        for i, item in enumerate(list):
            if item["name"]==required_keyword:
                item["name"]=new_name
                item["details"]=new_details
                item["sample_code"]=new_sample
                list[i]=item
                break

        else:
            print("Keyword Updated.")
    if flag==False:
        add_keyword.add_keyword(list,flag) 