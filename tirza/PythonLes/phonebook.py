'''Training 5: A phonebook
Write a mini database to store contact information (name, phone number and email address).
Use proper variablenames.
Use a list to store contact data. Contacts are also stored as lists.
Store the information as follows: [[<NAME>, <PHONE>, <EMAIL>], [<NAME>, <PHONE>, <EMAIL>]]
When the script is started, print the following:
    What to do?
    1. List entries
    2. Add entry
Use the input() function to build a working menu, a user enters 1 or 2 to pick an operation. 
Code the actual functionality:
Implement functionality 1: when the user chooses this, loop over the outer list and print every list in there on aseperate line.
Implement functionality 2: when the user chooses this, use input() three times to ask for the contact's name,phone number and email address.
'''

#Write a mini database to store contact information (name, phone number and email address).
#Use proper variablenames. [[<NAME>, <PHONE>, <EMAIL>], [<NAME>, <PHONE>, <EMAIL>]]
mini_db = [["bla", "061234567", "bla@bla.bla"]]
print("Phonebook")
print(8 * "-" )

#print option 1 : list entries
def phonebook_list():
    for entry in mini_db:
        print(entry)

#print option 2 : add entry
def phonebook_add():
    name = input("Enter Name: \n")
    phone = input("Enter Phonenumber: \n")
    email = input("Enter E-mail addres \n")
    entry = [name, phone, email]
    mini_db.append(entry)

#add functionality
while True:    
    print("Welcome: \n Press 1 to show entries \n Press 2 to add entry \n Press 3 to quit")
    answer = input("Choose your option: \n")
    if answer == "1":
        phonebook_list()
    elif answer == "2":
        phonebook_add()
    elif answer == "3":
        break
    else:
        print("Invalid Input, please try again. \n")
        continue
    




