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

def valid_phone(phone):
    return (len(phone) == 10 and isinstance(phone, int)) or phone == 'None'

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
            for c in contacts:
                print(c.get_id() + ": " + c.get_fname() + c.get_lname() + c.get_phone() + c.get_email())
            print(str(len(contacts)) + ": None")
            choice = input("Selection: ")
            while True:
                if choice > len(contacts):
                    choice = input("Please enter valid selection: ")
                else:
                    if choice == len(contacts):
                        continue
                    else:
                        book.delete(choice)
                    break

        elif choice == "3": # updating a contact
            pass
        elif choice == "4": # display contact book
            contacts = book.get_contacts()
            for i in range(len(contacts)):
                info = contacts[i]
                print("\n~~~~~~~~~~~~~~~~~~~~~~~")
                print("First Name: " + info[0])
                print("Last Name: " + info[1])
                print("Phone: " + info[2])
                print("Email: " + info[3])
                print("Date Created: " + str(info[4]))

        elif choice == "5": # Search for a Contact
            pass
        elif choice == "6": # clear database
            book.clear_database()
        elif choice == "7": # exit
            exit()
        else: # invalid
            print("Invalid Input")

if __name__ == '__main__':
    main()
