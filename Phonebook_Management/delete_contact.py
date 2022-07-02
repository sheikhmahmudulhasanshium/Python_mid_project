def delete_list(required_number,list):     
    confirmation_message=input("Do you want to delete the contact? Y/N: ")
    if confirmation_message=="Y" or confirmation_message=="y":
           
        for index,item in enumerate(list):
            for i,number in enumerate(item["Number"]):
                if(number == required_number)and(len(item["Number"])<=1):#for single contact number
                    
                    del list[index]
                    print(f"Current Contact List:\n{list}")
                    print("Contact deleted.")
                    break
                elif(number == required_number)and(len(item["Number"])>=2):#for multiple contact number
                    del item["Number"][i]
                    print(f"Current Contact List:\n{list}")
                    print("Contact deleted.")
                    break
            else:
                print("Contact not found")
            
        
    else:
        print("Cancelled.")
"""     for item in range(len(list)):
            if list[item]["Number"]==required_number:
                del list[item]
                break
   """        

def delete(list):
        if list:
            print("....................Delete Contact..........................")
            print(f"Previous Contact List:\n{list}")
            number_searched=input("Enter Phone Number to delete:")
            delete_list(number_searched,list)
        else:
            print("Can not delete from empty contact list.")
            #add_contact.add_new()
