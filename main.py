import re
from ContactBook import ContactBook
from Contact import Contact

conn_psycopg = None

def menu():
    print("\nWhat would you like to do?")
    print("1. Add a New Contact")
    print("2. Delete a Contact")
    print("3. Update a Contact")
    print("4. Get all Contacts")
    print("5. Search for a Contact")
    print("6. Clear Database")
    print("7. Exit")
    choice = input("Enter your choice: ")
    return choice

def search_Menu():
    print("\nSearch by...")
    print("1. ID")
    print("2. First Name")
    print("3. Phone Number")
    print("4. Back")
    choice = input ("Enter your choice: ")
    return choice

def edit_menu(c: Contact):
    print("\n" + c.get_id() + ": " + c.get_fname() + " " + c.get_lname() + " " + c.get_phone() + " " + c.get_email())
    print("What would you like to update?")
    print("1. First Name only")
    print("2. Last Name only")
    print("3. Phone Number Only")
    print("4. Email only")
    print("5. Everything")
    print("6. None")
    choice = input("Enter your choice: ")
    return choice

def print_contacts(contacts):
    for c in contacts:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~")
        print("First Name: " + c.get_fname())
        print("Last Name: " + c.get_lname())
        print("Phone: " + c.get_phone())
        print("Email: " + c.get_email())
        print("Date Created: " + c.get_dateAdded())

def contact_selection(contacts):
    valid_id = []
    for c in contacts:
        valid_id.append(str(c.get_id()))
        print(c.get_id() + ": " + c.get_fname() + " " + c.get_lname() + " " + c.get_phone() + " " + c.get_email())
    print("-1: None")
    choice = input("Selection: ")
    while True:
        if choice not in valid_id or choice != "-1":
            choice = input("Please enter valid selection: ")
        else:
            return choice

def valid_phone(phone):
    return (len(str(phone)) == 10 and isinstance(int(phone), int)) or phone == 'None'

def valid_email(email):
    pattern = r"^[A-Za-z0-9]+[.-_]*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+$"
    return email == 'None' or (re.match(pattern, email) is not None)

def main():
    print("Welcome to your Contact Book!")
    book = ContactBook()

    while True:
        choice = menu()
        if choice == "1": # adding a new contact
            print("\nInput the information for the new contact or enter None:")
            fn = input("First_name: ")
            ln = input("Last_name: ")
            phone = input("Phone: ")

            while True: # validate phone number
                if valid_phone(phone):
                    break
                phone = input("Input Valid Number: ")

            email = input("Email: ")
            while True:
                if valid_email(email):
                    break
                email = input("Input valid email address: ")

            success = book.add(Contact(first_name=fn, last_name=ln, phone=phone, email=email))
            if success:
                print("Your contact was added successfully!")
            else:
                print("Invalid Contact Information")

        elif choice == "2": # deleting a contact
            contacts = book.get_contacts()
            choice = contact_selection(contacts)
            if choice != "-1":
                book.delete(choice)

        elif choice == "3": # updating a contact
            print("Which Contact would you like to update?")
            choice = contact_selection(book.get_contacts())
            if choice == "-1": break
            contact = book.get_by_id(int(choice))[0]

            while True:
                choice = edit_menu(contact)

                if choice == "1": # first name only
                    fname = input("Enter new first name: ")
                    contact.set_fname(fname)
                    book.edit(contact)

                elif choice == "2": # last name only
                    lname = input("Enter new last name: ")
                    contact.set_lname(lname)
                    book.edit(contact)

                elif choice == "3": # phone number only
                    phone = input("Enter new phone number or None: ")
                    while valid_phone(phone) is False:
                        phone = input("INVALID! Enter new phone number or None: ")
                    contact.set_phone(phone)
                    book.edit(contact)

                elif choice == "4": # email only
                    email = input("Enter new email or None: ")
                    while valid_email(email) is False:
                        email = input("INVALID! Enter new email or None: ")
                    contact.set_email(email)
                    book.edit(contact)

                elif choice == "5": #everything
                    fname = input("Enter new first name: ")
                    contact.set_fname(fname)

                    lname = input("Enter new last name: ")
                    contact.set_lname(lname)

                    phone = input("Enter new phone number or None: ")
                    while valid_phone(phone) is False:
                        phone = input("INVALID! Enter new phone number or None: ")
                    contact.set_phone(phone)

                    email = input("Enter new email or None: ")
                    while valid_email(email) is False:
                        email = input("INVALID! Enter new email or None: ")
                    contact.set_email(email)

                    book.edit(contact)

                elif choice == "6": # none
                    break
                else:
                    print("Invalid Selection!")

        elif choice == "4": # display contact book
            contacts = book.get_contacts()
            print_contacts(contacts)

        elif choice == "5": # Search for a Contact
            while True:
                choice = search_Menu()

                if choice == "1": # search by ID
                    new_id = input("Please Enter a valid ID: ")
                    if isinstance(int(new_id), int):
                        contacts = book.get_by_id(int(new_id))
                        print_contacts(contacts)
                    else:
                        print("Not a valid ID")

                elif choice == "2": # search by first name
                    name = input("Please Enter a valid First Name: ")
                    contacts = book.get_by_name(name)
                    print_contacts(contacts)

                elif choice == "3": # search by phone number
                    phone = input("Please Enter a valid Phone Number: ")
                    if valid_phone(phone):
                        contacts = book.get_by_phone(int(phone))
                        print_contacts(contacts)
                    else:
                        print("Not a valid phone number!")

                elif choice == "4": # back
                    break
                else:
                    print("Invalid Entry")

        elif choice == "6": # clear database
            if book.clear_database():
                print("Database cleared successfully")
            else:
                print("Error clearing database")

        elif choice == "7": # exit
            exit()
        else: # invalid
            print("Invalid Input")

if __name__ == '__main__':
    main()
