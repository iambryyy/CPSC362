import os
import sqlite3 

class Contacts: 
    def __init__(self, user_email = None):  #None was included so that program could run even without email
        self.user_email = user_email
        self.database_name = f"{user_email}_contacts.db"

    def set_database_name(self, database_name):
        self.database_name = database_name
        
        if os.path.exists(self.database_name):
            return
        else:
            con = sqlite3.connect(self.database_name)
            cur = con.cursor()

            cur.execute(''' CREATE TABLE IF NOT EXISTS contacts (contact_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                        first_name TEXT NOT NULL, 
                        last_name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        address TEXT NOT NULL,
                        birthday TEXT NOT NULL,
                        phone_number TEXT NOT NULL)''')
            
            con.commit()
            con.close()
            
    def get_database_name(self):
        return self.database_name 
    
    def add_contact(self, first_name, last_name, email, address, birthday, phone_number):
        con = sqlite3.connect(self.database_name)
        cur = con.cursor()
        cur.execute('''INSERT INTO contacts (first_name, last_name, email, address, birthday, phone_number) VALUES (?,?,?,?,?,?) ''',
                    (first_name, last_name, email, address, birthday, phone_number))
        con.commit()
        con.close()
    
    def modify_contact(self, contact_id, first_name, last_name, email, address, birthday, phone_number):
        con = sqlite3.connect(self.database_name)
        cur = con.cursor()

        fields = [f"first_name = '{first_name}'",
                  f"last_name = '{last_name}'",
                  f"email = '{email}'",
                  f"address = '{address}'",
                  f"birthday = '{birthday}'",
                  f"phone_number = '{phone_number}'"]

        update_str = ', '.join([field for field in fields if field.split('=')[1].strip() != "None"])

        cur.execute(f'''UPDATE contacts SET {update_str} WHERE contact_id = ?''', (contact_id))
        con.commit()
        con.close()
    
    def get_contact(self):
        con = sqlite3.connect(self.database_name)
        cur = con.cursor()
        cur.execute('''SELECT * FROM contacts''')
        all_contacts = cur.fetchall()
        con.close()
        return all_contacts

    def delete_contact(self, contact_id):
        con = sqlite3.connect(self.database_name)
        cur = con.cursor()
        cur.execute('''DELETE FROM contacts WHERE phone_number = ?''',(contact_id))
        con.commit()
        con.close() 
    
   


