phonebook = [
    {
        'name' : 'Roel',
        'phone' : 1234567890,
        'email' : 'roel@roel.nl',
    }
]

def list_entries():
    for contact in phonebook:
        print(
'Name  :', contact['name'],
'\nPhone :', contact['phone'],
'\nEmail :', contact['email'],'\n'
        )

def add_entry():
    name = input('Enter name: ')
    phone = int(input('Enter phone number: '))
    email = input('Enter email address: ')
    contact = {
        'name' : name,
        'phone' : phone,
        'email' : email,
    }
    phonebook.append(contact)

while True:
    option = input('What to do?\n1. List entries\n2. Add entry\n3. Quit\n')
    # Option to list all saved entries.
    if option == '1':
        list_entries()
    # Option to add an entry.
    elif option == '2':
        add_entry()
    # Option to quit the script.
    elif option == '3':
        quit()
    # Fallback for when unssupported option is entered.
    else:
        print("Invalid input, please select '1', '2' or '3'.")
        continue