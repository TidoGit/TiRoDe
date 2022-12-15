import json

# Import phonebook from 'phonebook.json'.
def import_contacts():
    phonebook = json.load(open('phonebook.json', 'r'))
    return phonebook

# Export contacts to 'phonebook.json'.
def export_contacts(exp_contacts):
    phonebook = open('phonebook.json', 'w')
    json.dump(exp_contacts, phonebook, indent = 4)

# Print a contact.
def print_contact(contact):
    contacts = import_contacts()
    print(f'Email address  : {contact}')
    print(f'Contact ID     :', contacts[contact]['id'])
    print(f'Name{11*" "}:', contacts[contact]['name'].title())
    phone_num = 0
    for key, value in contacts[contact]['phone'].items():
        phone_num += 1
        if phone_num > 1: 
            print(f'Phone number {phone_num} : {value}')
        else:
            print(f'Phone number   : {value}')
    email_num = 0
    for key, value in contacts[contact]['alt_email'].items():
        email_num += 1
        if email_num > 1:
            print(f'Alt. address {email_num} : {value}')
        else:
            print(f'Alt. address   : {value}')
    print('\n')

# Add search result function
def search_result(contact, results):
    if contact in results:
        return results
    else:
        results.append(contact)
        return results

# Search for a contact.
def search_contacts():
    contacts = import_contacts()
    query = input("Enter search query. To search contact IDs; add '-id'.\n>>>")
    query = query.lower()
    index_trigger = '-id'
    results = []
    for contact in contacts:
        # Check for presence of '-id'.
        if index_trigger in query:
            query = int(query.strip('-id'))
            # Match ID.
            if query == contacts[contact]['id']:
                results = search_result(contact, results)
                continue
            else:
                break
        # Match primary email address.
        if query in contact:
            results = search_result(contact, results)
        # Match name.
        if query in contacts[contact]['name']:
            results = search_result(contact, results)
            continue
        # Match phone numbers.
        for key, value in contacts[contact]['phone'].items():
            if query in value:
                results = search_result(contact, results)
                continue
        # Match alternative email addresses. 
        for key, value in contacts[contact]['alt_email'].items():
            if query in value:
                results = search_result(contact, results)
                continue
    # Fallback
    if len(results) == 0:
        print('\n****No contacts match given query.')
    return results

# Add a contact.
def add_contact():
    contacts = import_contacts()
    pri_email = input('Enter primary email address:\n>>> ').lower()
    for contact in contacts:
        if pri_email in contacts.keys():
            print('\n****Email address already in use!')
            return
    name = input('Enter name:\n>>> ').lower()
    # Add multiple phone numbers.
    phone_index = 0
    phone_num = ''
    phone_numbers = {}
    while True:
        if phone_index == 0:
            phone_num = input('Enter phone number:\n>>> ')
            if len(phone_num) == 0:
                print('\n****Provide at least one phone number!')
                continue
        else:
            phone_num = input('Enter alternative phone number:\n>>> ')
        
        if phone_num != '':
            phone_numbers[f'phone{phone_index}'] = phone_num
            phone_index += 1
        else:
            break
    # Add multiple alternative email addresses.
    email_index = 0
    email_addr = ''
    email_addresses = {}
    while True:
        email_addr = input('Enter alternative email address:\n>>> ').lower()
        if email_index == 0:
            if len(email_addr) == 0:
                print('\n****Provide at least one alternative email address!')
                continue        
        if email_addr != '':
            email_addresses[f'email{email_index}'] = email_addr
            email_index =+ 1
        else:
            break
    # Create contact entry in contacts.
    id_num_list = []
    for contact in contacts:
        id_num_list.append(contacts[contact['id']])
    id_num = max(id_num_list) + 1
    contact_info = {
        'name' : name,
        'id' : id_num,
        'phone' : phone_numbers, 
        'alt_email' : email_addresses,
    }
    contacts[pri_email] = contact_info
    export_contacts(contacts)

# Delete a contact
def delete_contact():
    results = search_contacts()
    contacts = import_contacts()
    del_counter = 0
    for result in results:
        print_contact(result)
    del_confirm = input('Delete these contacts? (y/n):\n>>> ').lower()
    if del_confirm == 'y':
        for result in results:
            del contacts[result]
        export_contacts(contacts)
    else:
        print('\n****No contacts deleted.')


# Functionality
def menu():
    while True:
        choice = input('''What to do?\n1. List all contacts\n2. Search contact\
            \n3. Add contact\n4. Delete contact\n5. Quit \n>>> ''')
        if choice == '1':
            contacts = import_contacts()
            if len(contacts) == 0:
                print('\n****The phonebook is empty!')
            else:
                print('\n')
                for contact in contacts:
                    print_contact(contact)
        elif choice == '2':
            results = search_contacts()
            for result in results:
                print_contact(result)
        elif choice == '3':
            add_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            break
        else:
            print('\n****Invalid input, please choose 1, 2, 3, 4, or 5.')

if __name__ == '__main__':
    menu()