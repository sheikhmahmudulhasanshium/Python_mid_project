
def add_new(list,contact_name="",contact_address="",contact_email="",contact_numbers=[]):     
    contact={"Name":contact_name,"Address":contact_address,"Email":contact_email,"Number":contact_numbers}

    confirmation_message=input("Do you want to save the contact? Y/N: ")
    if confirmation_message=="Y" or confirmation_message=="y":
        list.append(contact)
        print(list)
        print("Contact added.")
    else:
        print("Cancelled.")


def add_existing(list,required_name,new_number):
    confirmation_message=input("Do you want to save the contact? Y/N: ")
    if confirmation_message=="Y" or confirmation_message=="y":
        for index,item in enumerate(list):
                if item["Name"]==required_name:
                    item["Number"].append(new_number)
                    print("Contact added.")
                    print(list)
                    break
        else:
            print("Contact not found")
        
    else:
        print("Cancelled.")

def add_contact(list):
    print("........................Add Contact.............................")
    p=("\n Enter 'n' to add new contact")
    p +=("\n Enter 'e' to add existing contact\n")
    u_input=input(p)
    if u_input=="n":
        print("....................Add New Contact..........................")
        contact_name=input("Enter contact Name:")
        contact_address=input("Enter Address:")
        contact_email=input("Enter Email:")
        contact_number=input("Enter Phone Number:")

        add_new(list,contact_name,contact_address,contact_email,[contact_number])
    elif u_input=="e":
        print("....................Add Existing Contact..........................")
        required_name=input("Enter name to add contact:")
        number=input("Enter Phone :")
        add_existing(list,required_name,number)
