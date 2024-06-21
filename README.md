# Contact-Book

Created by Rubi Dionisio

The Contact Book project is a robust command line tool that allows users to create, read, update, and delete contact details conveniently through the Click library. This project not only focuses on the basic functionality of storing and managing contacts but also, I hope to incorporate the extra challenge to enhance user data security through automatic and/or manual online backup.

## Technical Details
Commands will be implemented using the click command-line framework for users to enter contact details easily. A simple API will be established for ease of use. The Python psycopg3 module will be used to simply query the PostgreSQL database. Commands will support the ability to delete contacts, update contact information, and list saved contacts, allowing users to list contacts using different parameters like alphabetical order or contact creation date. PostgreSQL is chosen for its user-friendly setup, performance benefits, relational features, low cost, and I also have some experience with PostgreSQL. Utilizing the Python psycopg3 module will allow simple management of a cloud hosted instance of a PostgreSQL database for storing contact information.

## Extra Challenge: Online Database
Recognizing the potential risk of users losing contact details if their local files are compromised, an online database system will be implemented instead to mitigate this risk. A mechanism will be integrated to periodically upload the PostgreSQL database files to an online storage platform. Provided commands will allow users to manually backup the database to ensure they have control over their data. Or while the user is active, the application will send periodic updates to the database. To ensure the correct association between users and their respective databases, user-specific identification will be used to distinguish and match the appropriate database entities with each user. While implementing online storage, security measures must be prioritized to protect user data during transmission and storage.

The Contact Book project not only serves as a practical tool for contact management but goes beyond by addressing potential data loss concerns through the incorporation of an online database system with user authentication. This extra challenge enhances the overall robustness and user experience of the contact book software.

## Sources
* <a href="https://realpython.com/python-click/"> Click and Python: Build Extensible and Composable CLI Apps – Real Python </a>
* <a href="https://click.palletsprojects.com/en/8.1.x/"> Welcome to Click — Click Documentation (8.1.x) (palletsprojects.com) </a>
* <a href="https://www.psycopg.org/psycopg3/docs/index.html"> psycopg 3.2.0.dev1 documentation </a>
* <a href="https://www.postgresql.org/"> PostgreSQL: The world's most advanced open source database </a>

## Status
### Current Progress
```
    Currently implementing the contact book class:
        Add contact: DONE
        Delete Contact: DONE
        Update Contact: DONE
        Show Contacts: DONE
```

### Current Issues
```
    None
```

### Next Plan of Action
```
    More Unit testing if necessary
```

