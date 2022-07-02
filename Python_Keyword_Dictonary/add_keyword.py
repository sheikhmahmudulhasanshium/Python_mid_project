import search_keyword
def add_keyword(list,is_from_search):
    confirmation_message=input("Do you want to add the contact? Y/N: ")
    if confirmation_message=="Y" or confirmation_message=="y":
     
            if(is_from_search==False):
                print("....................Add Keyword..........................")
                key_name=input("Enter keyword name:")
                search_keyword.search_list(list,key_name)
                print("Can not add the key that already exists")
            
            elif(is_from_search==True):
                print("....................Add New Keyword..........................")
                key_name=input("Enter keyword name again to confirm:")
                details=input("Enter keyword's details:")
                code=input("Enter keyword's sample code:")
                keyword_info={"name":key_name,"details":details,"sample_code":code}
                list.append(keyword_info)
                
                print("Keyword added")
                print(list)
    else:
        print("Cancelled.")
       