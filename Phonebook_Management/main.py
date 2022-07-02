import add_contact,update_contact,delete_contact,search,display_contact,store_contact

#Empty list
contact_list=[]

print("..........................Contacts.............................")
while True:
    
    promt=("..........................Menu.................................")
    promt +=("\n Welcome user.")
    promt +=("\n Enter '+' to add contact")
    promt +=("\n Enter '-' to delete contact")
    promt +=("\n Enter 'x' to update contact")
    promt +=("\n Enter '?' to search contact")
    promt +=("\n Enter '.' to show contact list")
    promt +=("\n Enter 's' to save contact list in a file")
    promt +=("\n Enter 'quit' to quit the system\n")
    user_input=input(promt)
    if user_input=='+':
        add_contact.add_contact(contact_list)
    elif user_input=='x':
        update_contact.update(contact_list)
    elif user_input=="-":
        delete_contact.delete(contact_list)
    elif user_input=="?":
        search.search(contact_list)
    elif user_input==".":
        display_contact.display_list(contact_list)
    elif user_input=="s":
        store_contact.write(contact_list)
        print("Successfully saved contact")
        store_contact.read(contact_list)
    elif user_input=="quit":   
        break
    else:
        print("Enter correct option.")
