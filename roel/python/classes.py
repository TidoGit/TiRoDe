'''Introduction to classes.'''

class Phonebook:
    '''Phonebook class.'''

    def __init__(self):
        self.data = {}


    def print_contacts(self):
        '''Print all contacts'''
        print(self.data)


    def add_contact(self):
        '''Add contact to dict'''
        key = input()
        value = input()
        self.data.update({key:value})


    def delete_contact(self):
        '''Delete contact from dict'''
        key = input()
        self.data.pop(key)


    def search_contact(self):
        '''Search for contact in dict'''
        query = input()
        for instance in self.data.items():
            if query in instance:
                print(instance)
