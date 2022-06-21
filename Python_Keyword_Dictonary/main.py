import python_keywords,add_keyword,search_keyword,update_keyword,display_keywords,delete_keyword,store_keywords
keywords=python_keywords.keyword_list

print("..........................keywords.............................")
while True:
    
    promt=("..........................Menu.................................")
    promt +=("\n Welcome user.")
    promt +=("\n Enter '+' to add keyword")
    promt +=("\n Enter '-' to delete keyword")
    promt +=("\n Enter 'x' to update keyword")
    promt +=("\n Enter '?' to search keyword")
    promt +=("\n Enter '.' to show keyword list")
    promt +=("\n Enter 's' to save keyword list in a file")
    promt +=("\n Enter 'quit' to quit the system\n")
    user_input=input(promt)
    if user_input=='+':
        add_keyword.add_keyword(keywords,False)
    elif user_input=='x':
        update_keyword.update_keyword(keywords)
    elif user_input=="-":
        delete_keyword.delete(keywords)
    elif user_input=="?":
        flag=search_keyword.search(keywords)

    elif user_input==".":
        display_keywords.display_list(keywords)
    elif user_input=="s":
        store_keywords.write(keywords)
        print("Successfully saved keyword")
        store_keywords.read(keywords)
    elif user_input=="quit":   
        break
    else:
        print("Enter correct option.")

