import tkinter as tk
from tkinter import simpledialog, messagebox
from contacts import Contacts
from desktopnotif import *

window = None

def launch_contact_book(contact_db_instance):
    global window, contact_db
    
    #Placeholder where it will get the info from advancedLogging.py
    contact_db = contact_db_instance

    #title opening page when launched goes right
    window = tk.Tk()

    window.title('Contact Book')

    label = tk.Label(
    window,
    text = "Welcome",
    background = "white",
    foreground = "black",
    width = 1920,
    height = 1080
    )

    ##Actions for the command action when the button is pressed##
    #Action Function to add contact in the pop window
    def open_add_contact_window():
        add_window = tk.Toplevel(window)
        add_window.title("Add Contact")

        labels = ["First Name", "Last Name", "Email", "Address", "Birthday", "Phone Number"]
        entries = []

        for index, label_text in enumerate(labels):
            label = tk.Label(add_window, text=label_text)
            label.grid(row=index, column=0)
            entry = tk.Entry(add_window)
            entry.grid(row=index, column=1)
            entries.append(entry)
    
        def save_contact():   #Will execute once 'add_contact' gets fulfilled successfully
            details = [entry.get() for entry in entries]
            contact_db.add_contact(*details)
            messagebox.showinfo("Success", "Contact added successfully!") 
            add_window.destroy()
            contact_db.add_contact_listbox(contact_list, contact_db.get_contact()) #This makes added contact appear in listbox
    
        add_button = tk.Button(add_window, text="Add", command=save_contact)
        add_button.grid(row=len(labels), column = 1)   
        
        def add_contact_listbox(self):
            contact_list.delete(0, tk.END)   #this should clear listbox of duplicates
            contacts = self.get_contact()
            for contact in contacts:
                contact_list.insert(tk.END, f"{contact[1]} {contact[2]} - {contact[6]}")  

    #Action Function to delete contact in the pop window 
    def open_delete_contact_window():
        del_window = tk.Toplevel(window)
        del_window.title("Delete Contact")  

        labels = ["First Name", "Last Name", "Phone Number"]
        entries = []

        for index, label_text in enumerate(labels):
            label = tk.Label(del_window, text=label_text)
            label.grid(row=index, column=0)
            entry = tk.Entry(del_window)
            entry.grid(row=index, column=1)
            entries.append(entry)
    
        def confirm_delete():
            first_name, last_name, phone_number = [entry.get() for entry in entries]
            contact_db.delete_contact(first_name, last_name, phone_number)
            updated_contacts = contact_db.get_contact()      #updates current contacts 
            contact_db.add_contact_listbox(contact_list, updated_contacts)  #this will refresh listbox with new current contacts
            messagebox.showinfo("Success", "Contact deleted successfully!")
            del_window.destroy()
    
        del_btn = tk.Button(del_window, text="Delete", command=confirm_delete)
        del_btn.grid(row=len(labels), column=1)
        
        #array for Contact info 
        entry_first_name = entries[0]
        entry_last_name = entries[1]
        entry_email = entries[2]
        entry_address = entries[3]
        entry_birthday = entries[4]
        entry_phone_number = entries[5]
        

    def open_modify_contact_window():
        mod_window = tk.Toplevel(window)
        mod_window.title("Modify Contacts")

        labels = ["First Name", "Last Name", "Email", "Address", "Birthday", "Phone Number"]
        entries = []

        for index, label_text in enumerate(labels):
            label = tk.Label(mod_window, text=f"Current {label_text}")
            label.grid(row=index, column=0)
            entry = tk.Entry(mod_window)
            entry.grid(row=index, column=1)
            entries.append(entry)

        new_labels = ["New First Name", "New Last Name", "New Email", "New Address", "New Birthday", "New Phone Number"]
        new_entries = []
    
        def save_changes():
            first_name, last_name, email, address, birthday, phone_number = [entry.get() for entry in entries]
            details = [entry.get() for entry in new_entries]
            contact_db.modify_contact(first_name, last_name, email, address, birthday, phone_number, *details)
            messagebox.showinfo("Success!", "Contact has been modified successfully!")
            mod_window.destroy()
    
        mod_btn = tk.Button(mod_window, text="Modify", command=save_changes)
        mod_btn.grid(row=len(new_labels), column=3)

    #button for addCont
    addContactButton = tk.Button(
        window,
        text = "Add Contact",
        font=("Arial", 10, "bold"),
        width = 30,
        height = 30,
        background = "navy blue",
        foreground = "white"    
    )

    #button for delCont
    delContactButton = tk.Button(
        window,
        text = "Delete Contact",
        font=("Arial", 10, "bold"),
        width = 30,
        height = 30,
        background = "forest green",
        foreground = "white" 
    
    )
    
    
    

    ''''contacts_label = tk.Label(window, text="CURRENT CONTACTS")
    contacts_label.grid(row=0, column=0, columnspan=2)

    contact_list=tk.Listbox(window)
    contact_list.grid(row=1, column=1, columnspan=2, sticky=tk.NSEW)

    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0,weight=1)
    '''''
    
   # right side where contacts will be displayed  LAST UPDATE HERE
    contacts_label = tk.Label(
        window, 
        text="                CURRENT CONTACTS HERE",
        anchor = "n",
        font=("Arial", 45, "bold")
              )
    
    contacts_label.grid(row=0,column=1,sticky=tk.NW)
    contact_list = tk.Listbox(window)  #The actual textbox
    contact_list.grid(row=1, column=1, columnspan=5, sticky=tk.NSEW)
    window.grid_columnconfigure(1, weight = 1)  #this expands the column for 'listbox' horizontally
    window.grid_rowconfigure(1, weight = 1)

    #placements for the buttons to make them look more uniform
    delContactButton.grid(row=0, column=0, sticky="w")
    addContactButton.grid(row=1, column=0, sticky="w")

    #command actions when the button is clicked 
    addContactButton.config(command=open_add_contact_window)
    delContactButton.config(command=open_delete_contact_window)

    window.mainloop()

if __name__ == '__main__':
    contact_db = Contacts()
    launch_contact_book(contact_db)

    