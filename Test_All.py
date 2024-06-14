import unittest
from Contact import Contact
from ContactBook import ContactBook

class ContactBookTest(unittest.TestCase):
    def test_add_contact(self):
        c = Contact(first_name="Rubi", last_name="D", phone="1234567890", email="test@test.com")
        cb = ContactBook()

        self.assertTrue(cb.add(c))

    def test_delete_contact(self):
        c = Contact(first_name="Rubi", last_name="D", phone="1234567890", email="test@test.com")
        cb = ContactBook()
        cb.add(c)
        self.assertTrue(cb.delete(1))

    def test_clear_db(self):
        c = Contact(first_name="Rubi", last_name="D", phone="1234567890", email="test@test.com")
        cb = ContactBook()
        cb.add(c)
        self.assertTrue(cb.clear_database())


if __name__ == '__main__':
    unittest.main()
