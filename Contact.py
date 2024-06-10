import re
import datetime # used for saving information on when a new contact was created.

class Contact:
    def __init__(self, id = None, first_name=None, last_name=None, phone=None, email=None, date_added=None):
        if phone is None and email is None:
            raise ValueError("Phone or email must be added")

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.date_added = date_added if date_added is not None else datetime.datetime.now()

    def get_id(self):
        """ get id """
        return self.id

    def set_id(self, id):
        """ set contact id"""
        self.id = id

    def set_fname(self, name):
        """ sets first name """
        self.first_name = name

    def set_lname(self, name):
        """ sets last name """
        self.last_name = name

    def set_phone(self, phone):
        """ sets valid phone number """
        if (len(phone) == 10 and isinstance(phone, int)) or phone == 'None':
            self.phone = phone
            return True
        else:
            return False

    def set_email(self, email):
        """ sets a valid email address """
        pattern = r"^[A-Za-z0-9]+[.-_]*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+$"
        if email == 'None' or (re.match(pattern, email) is not None):
            self.email = email
            return True
        else:
            return False

    def get_fname(self):
        """return first name"""
        return self.first_name

    def get_lname(self):
        """return last name"""
        return self.last_name

    def get_phone(self):
        """return phone number"""
        return self.phone

    def get_email(self):
        """return email address"""
        return self.email

    def get_dateAdded(self):
        """return date created"""
        return self.date_added