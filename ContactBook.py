class ContactBook:
    def __init__(self, contacts={}):
        self.contacts = contacts
        self.number_of_contacts = len(self.contacts)

    def add(self, first_name=None, last_name=None, phone=None, email=None, created=None):
        """Adds a new contact to local contact book"""
        self.contacts[self.number_of_contacts] = [first_name, last_name, phone, email, created]
        self.number_of_contacts += 1

    def delete(self, index):
        """Deletes a contact from local contact book"""
        del self.contacts[index]

    def get_contacts(self):
        return self.contacts