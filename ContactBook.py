from Contact import Contact
import psycopg as pg
import os

class ContactBook:
    def __init__(self):
        self.conn = pg.connect(os.getenv("database_url"))
        self.cur = self.conn.cursor()

        try:
            create_table = 'CREATE TABLE IF NOT EXISTS contactBook (id SERIAL PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), phone INT, email VARCHAR(255), date_created VARCHAR(255));'
            self.cur.execute(create_table)
            self.conn.commit()

        except Exception as error:
            print(error)

            if self.conn is not None:
                self.conn.close()
            if self.cur is not None:
                self.cur.close()

    def clear_database(self):
        """Clears the database"""
        try:
            self.cur.execute('TRUNCATE contactBook; DELETE FROM contactBook;')
            self.conn.commit()
        except Exception as error:
            print(error)
            return False

        return True

    def add(self, contact: Contact):
        """Adds a new contact to local contact book"""
        try:
            add_contact = 'INSERT INTO contactBook (first_name, last_name, phone, email, date_created) VALUES (%s, %s, %s, %s, %s)'
            values = (
                contact.get_fname(), contact.get_lname(), contact.get_phone(), contact.get_email(),
                contact.get_dateAdded())
            self.cur.execute(add_contact, values)
            self.conn.commit()

        except Exception as error:
            print(error)
            return False
        return True

    def edit(self, contact: Contact):
        """ Edit contact information """
        try:
            insert_script = 'UPDATE FROM contactBook SET first_name = (%s), last_name = (%s), phone = (%s), email = (%s) WHERE id = %s'
            values = (
            contact.get_fname(), contact.get_lname(), contact.get_phone(), contact.get_email(), contact.get_id())
            self.cur.execute(insert_script, values)
            self.conn.commit()
        except pg.Error as error:
            print(error)

    def delete(self, index):
        """Deletes a contact from local contact book"""
        try:
            insert_script = 'DELETE FROM contactBook WHERE id = %s'
            self.cur.execute(insert_script, (index,))
            self.conn.commit()

        except Exception as error:
            print(error)
            return False
        return True

    def get_by_id(self, id:int):
        """Retrieve contact details by ID"""
        return self._run_sql_fetchall('SELECT * FROM contactBook WHERE id = %s', id)

    def get_by_name(self, name: str):
        """Retrieve contact details by name"""
        return self._run_sql_fetchall('SELECT * FROM contactBook WHERE LOWER(first_name) = LOWER(%s)', name)

    def get_by_phone(self, phone: int):
        """Retrieve contact details by phone number"""
        return self._run_sql_fetchall('SELECT * FROM contactBook WHERE phone = %s', phone)

    def get_contacts(self):
        try:
            self.cur.execute('SELECT * FROM contactBook')
            self.conn.commit()
            contacts = self.cur.fetchall()

        except pg.Error as error:
            print(error)
            return None
        return contacts

    def _run_sql_fetchall(self, script, **kwargs):
        try:
            self.cur.execute(script, (kwargs,))
            self.conn.commit()
            contact = self.cur.fetchall()

        except pg.Error as error:
            print(f"Error executing script: { script }\n\twith params: { kwargs }")
            return None
        return contact