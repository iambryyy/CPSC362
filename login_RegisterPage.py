from tkinter import *
from customtkinter import *
from tkinter import messagebox
from popwindow import launch_contact_book
from contacts import Contacts
import sqlite3

##### Sets the appearance of the window #####
set_appearance_mode("Dark")  

##### Sets the color of the widgets to this default color #####
set_default_color_theme("blue")

##### Dimensions of the Login Window #####
appWidth, appHeight = 600, 700

##### Create the database for the accounts created using the imports of sqlite3 #####
con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
            name text,
            email text,
            contact number,
            gender text,
            country text, 
            password text
            )
        ''')
con.commit()

########## REGISTER PAGE WINDOW ########
def open_register_window():

    register_window = CTkToplevel()
    register_window.title("Register Window")
    register_window.geometry(f'{appWidth}x{appHeight}')

    ###### REGISTRATION FUNCTION RESPONSE ######
    def insert_record():
        # Gather all inputs
        name = nameEntry.get()
        email = emailEntry.get()
        contact = mobileEntry.get()
        gender = gendervar.get()
        states = statesVariable.get()
        pwd = passEntry.get()
        pwd_reenter = passReEnterEntry.get()
        
        # Check each input and store associated error messages
        errors = []
        if not name:
            errors.append("Name can't be empty")
        if not email:
            errors.append("Email can't be empty")
        if not contact:
            errors.append("Contact can't be empty")
        if not gender:
            errors.append("Select Gender")
        if not states:
            errors.append("Select State")
        if not pwd:
            errors.append("Password can't be empty")
        if pwd != pwd_reenter:
            errors.append("Passwords didn't match")
        
        # If there are errors, show the first error from the list
        if errors:
            messagebox.showerror("Error", errors[0])
            return
        
        #If there are no errors, check for email addresses uniquness
        try:
            con = sqlite3.connect('userdata.db')
            cur = con.cursor()
            cur.execute("SELECT * FROM  record WHERE email = ?", (email,))
            if cur.fetchone() is not None:
                messagebox.showerror('Error', 'This email is already registerd.')
                return 
        except Exception as ep:
            messagebox.showerror('',ep)
            return
        
        # If there are no errors, proceed with database insertion
        try:
            con = sqlite3.connect('userdata.db')
            cur = con.cursor()
            cur.execute("INSERT INTO record VALUES (:name, :email, :contact, :gender, :country, :password)",
                {
                    'name': name,
                    'email': email,
                    'contact': contact,
                    'gender': gender,
                    'country': states,
                    'password': pwd
                 })
            con.commit()
            messagebox.showinfo('confirmation','Record Saved')
        except Exception as ep:
            messagebox.showerror('', ep)
        finally:
            con.close()  #Ensures that the connection is closed whether there is an error or not 
        
        register_window.destroy()

    #Name Label 
    nameLabel = CTkLabel(master = register_window, text = "Enter Name")
    #Name Entry Field 
    nameEntry = CTkEntry(master = register_window, placeholder_text = "Ex.Bob")

    #Email Label
    emailLabel = CTkLabel(master = register_window, text = "Enter Email")
    #Email Entry Field
    emailEntry = CTkEntry(master = register_window, placeholder_text = "abc@gmail.com")

    #Contact Number Label
    mobileLabel = CTkLabel(master = register_window, text = "Contact Number")
    #Contact Number Entry Field 
    mobileEntry = CTkEntry(master = register_window, placeholder_text = "123-456-7890")

    #Gender Label
    genderLabel = CTkLabel(master = register_window, text = "Gender")
    #Gender Radio Buttons
    gendervar = StringVar(master = register_window, value = "Prefer \
                          not to say")
    maleRadioButton = CTkRadioButton(master = register_window, text = "Male", variable = gendervar)
    femaleRadioButton = CTkRadioButton(master = register_window, text = "Female", variable = gendervar)
    noneRadioButton = CTkRadioButton(master = register_window, text = "Prefer Not to Say", variable = gendervar)

    ### References to the text file 'naStates.txt' to pass the information when registering account ###
    location = []
    statesVariable = StringVar()
    with open("naStates.txt", 'r') as USA:
        for states in USA:
            states = states.rstrip('\n')
            location.append(states)
    if len(location) > 49:
        statesVariable.set(location[49])

    #States Label
    statesOptionMenu = CTkOptionMenu(master = register_window, variable = statesVariable, values = location)

    #Pasword Label
    passLabel = CTkLabel(master = register_window, text= "Enter Password")
    #Password Entry
    passEntry = CTkEntry(master = register_window, show = "*")

    #Re-Enter Password Label
    passReEnterLabel = CTkLabel(master = register_window, text = "Re-Enter Password")
    #Re-Enter Password Entry
    passReEnterEntry = CTkEntry(master = register_window, show = "*")

    #Register Button
    registerButton = CTkButton(master = register_window, text = "Register", command = insert_record)

    ######## REGISTER WINDOW WiDGET PLACEMENT ########
    nameLabel.grid(row = 0, column = 0, padx = 20, pady = 20, sticky = "ew")
    nameEntry.grid(row = 0, column = 1, columnspan = 3, padx = 20, pady = 20, sticky = "ew")
    emailLabel.grid(row = 1, column = 0, padx = 20, pady = 20, sticky = "ew")
    emailEntry.grid(row = 1, column = 1, columnspan = 3, padx = 20, pady = 20, sticky = "ew")
    mobileLabel.grid(row = 2, column = 0, padx = 20, pady = 20, sticky = "ew")
    mobileEntry.grid(row = 2, column = 1, columnspan = 3, padx = 20, pady = 20, sticky = "ew")
    ### Gender Radio Button ###
    genderLabel.grid(row = 3, column = 0, padx = 20, pady = 20, sticky = "ew")
    maleRadioButton.grid(row = 3, column = 1, padx = 20, pady = 20, sticky = "ew")
    femaleRadioButton.grid(row = 3, column = 2, padx = 20, pady = 20, sticky = "ew")
    noneRadioButton.grid(row = 3, column = 3, padx = 20, pady = 20, sticky = "ew")
    ###########################
    statesOptionMenu.grid(row = 4, column = 1, padx = 20, pady = 20, columnspan = 2, sticky = "ew")
    passLabel.grid(row = 5, column = 0, padx = 20, pady = 20, sticky = "ew")
    passEntry.grid(row = 5, column = 1, padx = 20, pady = 20, sticky = "ew")
    passReEnterLabel.grid(row = 6, column = 0, padx = 20, pady = 20, sticky = "ew")
    passReEnterEntry.grid(row = 6, column = 1, padx = 20, pady = 20, sticky = "ew")
    registerButton.grid(row = 7, column = 1, pady = (0,10))

###### LOGIN FUNCTION RESPONSE ######
def login_response():
    uname = user_entry.get()
    upwd = pass_entry.get()

    try:
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        c.execute("SELECT * from record WHERE email = ? AND password = ?", (uname, upwd))
        user_record = c.fetchone()
        if user_record:
            messagebox.showinfo('Login Status', 'Logged in Successfully!')

            user_contacts = Contacts(uname)
           
            #Launch the main GUI
            launch_contact_book(user_contacts)
             
        else:
            messagebox.showerror('Login Status', 'Invalid Username or password')
    except Exception as ep:
        messagebox.showerror('', ep)
    finally:
        con.close()

########## LOGIN PAGE WINDOW ###########
##### Frame of the Login Page Window #####
main_frame = CTk()
main_frame.title("Desktop Login")
main_frame.geometry(f'{appWidth}x{appHeight}')

#Email "Username" Label
user_label = CTkLabel(master = main_frame, text = "Email:" )
#Email "Username" Entry
user_entry = CTkEntry(master = main_frame)

#Password Label
pass_label = CTkLabel(master = main_frame, text = "Password: ")
#Password Entry 
pass_entry = CTkEntry(master = main_frame, show = "*")

#Remember Me Check Button
remember_me = CTkCheckBox(master = main_frame, text = "Remember Me")

#Register Now Button
account_register = CTkButton(master = main_frame, text = "Register", command = open_register_window)

#Login Button 
login_button = CTkButton(master = main_frame, text = "Login", command = login_response, fg_color = 'green')

######## LOGIN WINDOW WIDGET PLACEMENT ########
user_label.grid(row = 1, column = 0, sticky = "w", pady = (0,10))
user_entry.grid(row = 1, column = 1, padx = 10, pady = (0,10))
pass_label.grid(row = 2, column = 0, sticky = "w", pady = (0,10))
pass_entry.grid(row = 2, column = 1, padx = 10, pady = (0,10))
remember_me.grid(row = 3, column = 1, pady = (0,10))
login_button.grid(row = 4, column = 1, pady = (0,20), sticky = "e")
account_register.grid(row = 4, column = 0, pady = (0,20), sticky = "e")

main_frame.mainloop()
