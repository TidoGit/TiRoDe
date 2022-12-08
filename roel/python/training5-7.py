phonebook = [
    [
        'Roel',
        1234567890,
        'roel@roel.nl',
    ],
]

# Function to list al entries in phonebook.
def list_entries():
    for contact in phonebook:
        print(contact)
    print(10 * '-')

# Function to add an entry to phonebook.
def add_entry():
    name = input('Enter name: ')
    phone_number = input('Enter phone number: ')
    email = input('Enter email address: ')
    contact = [name.title(), int(phone_number), email.lower()]
    phonebook.append(contact)
    print(10 * '-')

while True:
    option = input('What to do?\n1. List entries\n2.Add entry\n3. Quit\n')
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