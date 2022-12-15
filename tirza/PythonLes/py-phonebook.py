#Define a function to menu the user and provide options on how the phonebook works
def menu():
    #Create an entry variable using the input function and multiple line strings format
    menu_choice = int(input("""
                    Py Phonebook.  

                    1. Show all entries
                    2. Create a new entry
                    3. Update an entry 
                    4. Delete an entry
                    5. Exit
                    Enter your entry here(1,2,3,4 or 5):  """))
    
    #Close the function    
    return menu_choice

#phonebook file
mini_db = [{
    "ID#"    : 0,
    "Name"   : "bla", 
    "Number" : "061234567", 
    "E-mail" : "bla@bla.bla"
    }, {
    "ID#"    : 1,
    "Name"   : "John Smith", 
    "Number" : "061234567", 
    "E-mail" : "John.S@blabla.com"
    }]    

#updates the phonebook file
def phonebook_refresh():    
    index_num = -1
    for entry in mini_db:
        index_num += 1
        entry["ID#"] = index_num

#create a formatted list of all entries
def phonebook_list(entry):
    phonebook_refresh()
    print("ID#    : " + str(entry["ID#"]))
    print("Name   : " + entry["Name"])
    print("Number : " + entry["Number"])
    print("E-mail : " + entry["E-mail"])
    print(24 * "-")

#add a new entry
def phonebook_add():
    name = input("Enter Name: \n")
    phone = input("Enter Phonenumber: \n")
    email = input("Enter E-mail addres \n")
    entry = {"ID#" : "", "Name" : name, "Number" : phone, "E-mail" : email}
    mini_db.append(entry)
    #Print a success message
    print("Entry successfully saved")
    phonebook_refresh()

#delete the entry yes or no
def phonebook_delete(entry):
    phonebook_list(entry)
    yesorno = input("would you like to delete:\n (Y)yes or (N)o ?")
    if yesorno.lower() == "y":
        del mini_db[entry["ID#"]]
        print("Entry successfully deleted")
        phonebook_refresh()
    else:
        menu()

#find an entry and ask for delete yes or no
def find_entries():
    find_entry = input("Enter your search:\n")
    try:
        find_entry = int(find_entry)
        max_input = len(mini_db) -1
        if find_entry <= max_input:
            entry = mini_db[find_entry]
            phonebook_delete(entry)

        else:
            print("No such entry")
    except:
        find_entry = str(find_entry)
        for entry in mini_db:
            if find_entry in entry["E-mail"]:
                phonebook_delete(entry)
            else:
                break
    
#initiate a while loop to continuously run the phonebook program
while True:
    menu_choice = menu()
    #Option 1 List all
    if menu_choice == 1:
        #For first entry Check if contact dict is empty
        #If not empty,i.e bool(contact)==False, Print current contact list
        if bool(mini_db) != False:
            print("\n")
            for entry in mini_db:
                phonebook_list(entry)
        else:
            print('You have an empty phonebook! Go back to the menu to add a new contact')
    #Option 2 add entry
    elif menu_choice == 2:
        #run phonebook_add
        print("\n")
        phonebook_add()
    #Option 3 update entry
    elif menu_choice == 3:
        find_entries()
                
    #Option 4 delete entry
    elif menu_choice == 4:
        find_entries()

    #Option 5 Quit
    elif menu_choice == 5:
        print('Thanks for using the Py Phonebook')
        break
            
    #Error Message    
    else:
        print('Incorrect Entry!')
           
            
    #End of Program
