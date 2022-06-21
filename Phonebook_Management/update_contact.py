def update_list(required_number,list,contact_name="",contact_address="",contact_email="",contact_number=[]):     
    #contact={"Name":contact_name,"Address":contact_address,"Email":contact_email,"Number":contact_number}

    confirmation_message=input("Do you want to update the contact? Y/N: ")
    if confirmation_message=="Y" or confirmation_message=="y":
        for i,item in enumerate(list):
            for number in (item["Number"]):
                if(number == required_number):
                    item["Name"]=contact_name
                    item["Email"]=contact_email
                    item["Address"]=contact_address
                    item["Number"]=[contact_number]
                    list[i] = item
                    print("Contact updated.")
                    print(list)
                    break
        else: #end of list 
            print("Contact not found")   
        
        

    else:
        print("Cancelled.")

def update(list):
        print("....................Update Contact..........................")
        number_searched=input("Enter Phone Number To Update:")
        
        
        print("................Update Contact Information...............")
        contact_name=input("Enter New contact Name:")
        contact_address=input("Enter New Address:")
        contact_email=input("Enter New Email:")
        contact_number=input("Enter New Phone Number:")
        update_list(number_searched,list,contact_name,contact_address,contact_email,[contact_number])
