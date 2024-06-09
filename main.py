from ContactBook import ContactBook
from Contact import Contact

conn_psycopg = None


def menu():
    print("\nWhat would you like to do?")
    print("1. Add a New Contact")
    print("2. Delete a Contact")
    print("3. Update a Contact")
    print("4. Get all Contacts")
    print("5. Backup Contacts")
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice

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
                if book.valid_phone(phone):
                    break
                phone = input("Input Valid Number: ")

            email = input("Email: ")
            while True:
                if book.valid_email(email):
                    break
                email = input("Input valid email address: ")

            book.add(fn, ln, phone, email, current_time)
            print("Your contact was added successfully!")

        elif choice == "2": # deleting a contact
            contacts = book.get_contacts()
            for i in range(len(contacts)):
                info = contacts[i]
                print(str(i) + ": " + info[0] + info[1] + info[2] + info[3])
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
                print("Date: " + str(info[4]))

        elif choice == "5": # backup to database
            pass
        elif choice == "6": # exit
            exit()
        else: # invalid
            print("Invalid Input")

if __name__ == '__main__':
    main()
