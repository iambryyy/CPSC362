import json
import os
import sqlite3 

class contacts: 
    def __init__(self):
        self.database_name = "" 
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
        return self.get_database_name 
    
    def add_contact(self, first_name, last_name, email, address, birthday, phone_number):
        con = sqlite3.connect(self.database_name)
        cur = con.cursor()
        cur.execute('''INSERT INTO contacts (first_name, last_name, email, address, birthday, phone_number) VALUES (?,?,?,?,?,?) ''',
                    (first_name, last_name, email, address, birthday, phone_number))
        con.commit()
        con.close()

    def delete_contact(self, first_name, last_name, phone_number):
        con = sqlite3.connect(self.database_name)
        cur = con.cursor()
        cur.execute('''DELETE FROM contacts WHERE phone_number = ?''',(phone_number))
        con.commit()
        con.close() 

    def modify_contact(self, first_name, last_name, email, address, birthday, phone_number):
        con = sqlite3.connect(self.database_name)
        cur = con.cursor()
        cur.execute('''UPDATE contacts SET first_name = ?, last_name = ?, email = ?, address = ?, birthday = ? phone_number = ? WHERE phone_number = ?''',
                    (first_name, last_name, email, address, birthday, phone_number))
        con.commit()
        con.close()

    def geoLocationFeature():
