import os
import sqlite3 

class Contacts: 
    def __init__(self, user_email = None):  #None was included so that program could run even without email
        self.user_email = user_email #Email must be used to distinguish unique-ness in case contacts have same first/last name
        self.database_name = f"{user_email}_contacts.db"
        self.create_contacts_table()
        
    

    def create_contacts_table(self):
            con = sqlite3.connect(self.database_name)
            cur = con.cursor()
            cur.execute(''' CREATE TABLE IF NOT EXISTS contacts 
                        (contact_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
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
        
    def add_contact_listbox(self, contact_list):  #This allows contacts from add_contact function to actually populate the screen 
        contacts = self.get_contact()
        for contact in contacts:
            contact_list.insert(0, f"{contact[1]} {contact[2]} - {contact[5]}")
    
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
    
   


