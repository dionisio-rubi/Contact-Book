from Contact import Contact
import psycopg as pg
import requests

class ContactBook:
    def __init__(self, contacts=None):
        self.contacts = contacts if contacts is not None else {}
        self.number_of_contacts = len(self.contacts)

        # database connection
        host_name = 'ep-damp-forest-a6udjchs.us-west-2.aws.neon.tech'
        name = 'contacts'
        username = 'dionisio-rubi'
        password = 'SPD8Wxy1NbhX'

        try:
            conn = pg.connect(host=host_name, dbname=name, user=username, password=password)
            cur = conn.cursor()
            create_table = 'CREATE TABLE IF NOT EXISTS contactBook (id INT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), phone INT, email VARCHAR(255), date_created VARCHAR(255));'
            cur.execute(create_table)
            conn.commit()
        except Exception as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
            if cur is not None:
                cur.close()

    def add(self, contact: Contact):
        """Adds a new contact to local contact book"""
        self.contacts[self.number_of_contacts] = contact
        self.number_of_contacts += 1
        return True

    def edit(self, id):
        """ Edit contact information """
        pass

    def delete(self, index):
        """Deletes a contact from local contact book"""
        del self.contacts[index]

    def get_by_id(self, id):
        """Retrieve contact details by ID"""
        pass

    def get_by_name(self, name):
        """Retrieve contact details by name"""
        pass

    def get_by_phone(self, phone):
        """Retrieve contact details by phone number"""
        pass

    def get_contacts(self):
        return self.contacts