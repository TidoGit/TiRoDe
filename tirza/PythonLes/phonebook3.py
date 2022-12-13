#Write a mini database to store contact information (name, phone number and email address).
#Use proper variablenames. [[<NAME>, <PHONE>, <EMAIL>], [<NAME>, <PHONE>, <EMAIL>]]
mini_db = [{
    "Name"   : "bla", 
    "Number" : "061234567", 
    "E-mail" : "bla@bla.bla"
    }, {
    "Name"   : "John Smith", 
    "Number" : "061234567", 
    "E-mail" : "John.S@blabla.com"
    }]

print("Phonebook")
print(8 * "-" )

#print option 1 : list entries
def phonebook_list(entry):
    #for entry in mini_db:
        #print(entry)
        print("Name   : " + entry["Name"])
        print("Number : " + entry["Number"])
        print("E-mail : " + entry["E-mail"])
        print(24 * "-")

#print option 2 : add entry
def phonebook_add():
    name = input("Enter Name: \n")
    phone = input("Enter Phonenumber: \n")
    email = input("Enter E-mail addres \n")
    entry = {"Name" : name, "Number" : phone, "E-mail" : email}
    mini_db.append(entry)

#find and destroy!
def phonebook_delete(entry):
    phonebook_list(entry)
    yesorno = input("would you like to delete:\n (Y)yes or (N)o ?")
    if yesorno.lower() == "y":
        del mini_db[entry]
    else:
        phonebook_change()

def phonebook_change():
    print("Changing entries\n")
    find_entry = input("Enter your search:\n")
    try:
        find_entry = int(find_entry)
        max_input = len(mini_db) -1
        if find_entry <= max_input:
            entry = mini_db[find_entry]
            phonebook_delete(entry)
    except:
        find_entry = str(find_entry)
        for entry in mini_db:
            if find_entry in entry["E-mail"]:
                phonebook_delete(entry)
            else:
                break

#add functionality
while True:    
    print("\nWelcome: \n Press 1 to show entries \n Press 2 to change entries \n Press 3 to quit")    
    answer = input("Choose your option: \n")
    if answer == "1":
        print("\n")
        for entry in mini_db:
            phonebook_list(entry)
    elif answer == "2":
        print("\n")
        phonebook_change()
    elif answer == "3":
        break
    else:
        print("Invalid Input, please try again. \n")