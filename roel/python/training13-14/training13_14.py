'''
Contact managing tool which stores data in dicts inside a dict. The main dict
uses a contact's main email address as the unique identifier.

Adding contacts or displaying a specific contact's data is done through their
email address.

Writes the main dictionary into file 'phonebook.json' and loads from this file
when needed.
'''

import json


def import_contacts():
    '''Import phonebook from 'phonebook.json'.'''
    with open('phonebook.json', 'r', encoding='UTF-8') as file:
        phonebook = json.load(file)
    return phonebook


def export_contacts(exp_contacts):
    '''Export contacts to 'phonebook.json'.'''
    with open('phonebook.json', 'w', encoding='UTF-8') as file:
        json.dump(exp_contacts, file, indent = 4)


def print_contact(contact):
    '''Print a contact.'''
    contacts = import_contacts()
    print(f'Email address  : {contact}')
    print('Contact ID     :', contacts[contact]['id'])
    print(f'Name{11*" "}:', contacts[contact]['name'].title())
    phone_num = 0
    for key in contacts[contact]['phone']:
        phone_num += 1
        value = contacts[contact]['phone'].get(key)
        if phone_num > 1:
            print(f'Phone number {phone_num} : {value}')
        else:
            print(f'Phone number   : {value}')
    email_num = 0
    for key in contacts[contact]['alt_email']:
        email_num += 1
        value = contacts[contact]['alt_email'].get(key)
        if email_num > 1:
            print(f'Alt. address {email_num} : {value}')
        else:
            print(f'Alt. address   : {value}')
    print('\n')


def search_result(contact, results):
    '''Add search result function.'''
    if contact not in results:
        results.append(contact)
    return results


def search_contacts():
    '''Search for a contact.'''
    contacts = import_contacts()
    query = input("Enter search query. To search contact IDs; add '-id'.\n>>> ")
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
                break
        # Match primary email address.
        if query in contact:
            results = search_result(contact, results)
        # Match name.
        if query in contacts[contact]['name']:
            results = search_result(contact, results)
            continue
        # Match phone numbers.
        for key in contacts[contact]['phone']:
            if query in contacts[contact]['phone'].get(key):
                results = search_result(contact, results)
                continue
        # Match alternative email addresses.
        for key in contacts[contact]['alt_email']:
            if query in contacts[contact]['alt_email'].get(key):
                results = search_result(contact, results)
                continue
    # Fallback
    if len(results) == 0:
        print('\n**** No contacts match given query.')
    return results


def add_contact():
    '''Add a contact.'''
    contacts = import_contacts()
    pri_email = input('Enter primary email address:\n>>> ').lower()
    for contact in contacts:
        if pri_email in contacts.keys():
            print('\n**** Email address already in use!')
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
                print('\n**** Provide at least one phone number!')
                continue
        else:
            phone_num = input('Enter alternative phone number:\n>>> ')
        if phone_num == '':
            break
        phone_numbers[f'phone{phone_index}'] = phone_num
        phone_index += 1
    # Add multiple alternative email addresses.
    email_index = 0
    email_addr = ''
    email_addresses = {}
    while True:
        email_addr = input('Enter alternative email address:\n>>> ').lower()
        if email_index == 0:
            if len(email_addr) == 0:
                print('\n**** Provide at least one alternative email address!')
                continue
        if email_addr == '':
            break
        email_addresses[f'email{email_index}'] = email_addr
        email_index += 1
    # Create contact entry in contacts.
    id_num_list = []
    for contact in contacts:
        id_num_list.append(contacts[contact]['id'])
    id_num = max(id_num_list) + 1
    contact_info = {
        'name' : name,
        'id' : id_num,
        'phone' : phone_numbers,
        'alt_email' : email_addresses,
    }
    contacts[pri_email] = contact_info
    export_contacts(contacts)


def delete_contact():
    '''Delete a contact.'''
    results = search_contacts()
    contacts = import_contacts()
    for result in results:
        print_contact(result)
    del_confirm = input('Delete these contacts? (y/n):\n>>> ').lower()
    if del_confirm == 'y':
        for result in results:
            del contacts[result]
        export_contacts(contacts)
    else:
        print('\n**** No contacts deleted.')


def main():
    '''Main menu'''
    while True:
        choice = input('''What to do?\n1. List all contacts\n2. Search contact\
            \n3. Add contact\n4. Delete contact\n5. Quit \n>>> ''')
        if choice == '1':
            contacts = import_contacts()
            if len(contacts) == 0:
                print('\n**** The phonebook is empty!')
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
            print('\n**** Invalid input, please choose 1, 2, 3, 4, or 5.')


if __name__ == '__main__':
    main()
