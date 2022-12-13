phonebook = [
    {
        'name' : 'Roel',
        'phone' : {
            'phone0' : 1234567890, 
        },
        'email' : {
            'email0' : 'roel@roel.nl',
        },
    },
]

# Print phonebook contact.
def print_entry(argument):
    print('\nName  :', argument['name'],'\nPhone :')
    for key, value in argument['phone'].items():
        print('       ', value)
    print('Email :')
    for key, value in argument['email'].items():
        print('       ', value)

# List phonebook contacts.
def list_entries():
    # Check for contacts in phonebook.
    if len(phonebook) == 0:
        print('\nThere are no contacts in the phonebook.\n')
    else:
        for contact in phonebook:
            print_entry(contact)

# Search contacts in phonebook.
def search_entries():
    search_string = input('Enter your search string: ')
    # Check if search_string is a number.
    try:
        search_string = int(search_string)
        # Check if index number is not higher than total amount of contacts.
        if search_string > len(phonebook):
            print('\nThere are not so many contacts in the phonebook.\n')
            quit()
        else:
            search_result = phonebook[search_string]
            return search_result, search_string
    except:
        index_num = ( -1 )
        for contact in phonebook:
            index_num += 1
            for key, value in contact['email'].items():
                if search_string in value:
                    return contact, index_num
            else:
                print('''
Invalid input, only index number or email address allowed.
''')
    
def add_entry():
    name = input('Enter name: ')
    # Add multiple phone numbers in a dictionary.
    phone_index = 0
    phone_num = 0
    phone_numbers = {}
    while True:
        try:
            phone_num = int(input('Enter phone number :'))
        except:
            break
        phone_numbers[f'phone{phone_index}'] = phone_num
        phone_index += 1
    # Add multiple email addresses in a dictionary.
    email_index = 0
    email_addr = None
    email_addresses = {}
    while True:
        email_addr = input('Enter email address: ')
        if email_addr == '':
            break
        else:
            email_addresses[f'email{email_index}'] = email_addr
            email_index += 1
    # Add contact to phonebook.
    contact = {
        'name' : name,
        'phone' : phone_numbers,
        'email' : email_addresses,
    }
    phonebook.append(contact)

def remove_entry():
    result, index_num = search_entries()
    print_entry(result)
    del_option = input('Do you really want to delete this contact? (y/n) ')
    if del_option == 'y':
        del phonebook[index_num]
    else:
        print('Nothing was deleted.')

while True:
    option = input('''What to do?
1. List entries
2. Add entry
3. Remove entry
4. Quit
''')
    # List contacts.
    if option == '1':
        while True:
            list_choice = input('''Would you like to:
1. List all entries
2. Search for a specific entry
''')
            # List all contacts.
            if list_choice == '1':
                list_entries()
                print(phonebook)
                break
            # Search for a specific contact.
            elif list_choice == '2':
                result, index_num = search_entries()
                print_entry(result)
                break
            else:
                print("Invalid input, please select '1' or '2'.")
                continue
    # Option to add a contact.
    elif option == '2':
        add_entry()
    # Option to remove a contact.
    elif option == '3':
        remove_entry()
    # Option to quit the script.
    elif option == '4':
        quit()
    # Fallback for when unsupported option is entered.
    else:
        print("Invalid input, please select '1' to '4'.")
        continue
