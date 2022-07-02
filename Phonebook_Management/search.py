import add_contact
def search_by_name(list,searched_name):
    print("....................Search Contact..........................")
    for index,item in enumerate(list):
        
            if(item["Name"] == searched_name):
                print("Contact Found.") 
                print(list[index])
                break
                
    else:#end of loop reached
        print("Contact not found.")
       # add_contact.add_contact(list)
def search(list):
        if list:
            print("....................Search Contact..........................")
            required_keyword=input("Enter contact to search:")
            search_by_name(list,required_keyword)
        else:
            print("Can not search from empty contact list.")
            #add_contact.add_contact(list)