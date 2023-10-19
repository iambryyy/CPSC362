from tkinter import *
from tkinter import messagebox
from popwindow import launch_contact_book
from contacts import Contacts
import sqlite3

'''Creating the Database for the accounts created using the imports of sqlite3'''
f = ("Times", 14)

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

'''Configuration for the pop window'''
ws = Tk()
ws.title("Contact Book Login")
ws.geometry('940x500')
ws.config(bg = '#0B5A81')

'''Function Registering an Account for your contact book'''
def insert_record():

    # Gather all inputs
    name = register_name.get()
    email = register_email.get()
    contact = register_mobile.get()
    gender = var.get()
    country = variable.get()
    pwd = register_pwd.get()
    pwd_reenter = pwd_again.get()

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
    if not country:
        errors.append("Select Country")
    if not pwd:
        errors.append("Password can't be empty")
    if pwd != pwd_reenter:
        errors.append("Passwords didn't match")

    # If there are errors, show the first error from the list
    if errors:
        messagebox.showerror("Error", errors[0])
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
                        'country': country,
                        'password': pwd
                    })
        con.commit()
        messagebox.showinfo('confirmation','Record Saved')
        user_contacts = Contacts(email)
        launch_contact_book(user_contacts)
    except Exception as ep:
        messagebox.showerror('', ep)

'''Fuction for the Login in sequence'''
def login_response():
    try:
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        for row in c.execute("Select * from record"):
            username = row[1]
            pwd = row[5]
    except Exception as ep:
        messagebox.showerror('',ep)
    
    #Validations/Error Checking for Login
    uname = email_tf.get()
    upwd = pwd_tf.get()
    check_counter = 0 

    if uname == "":
        warn = "Username can't be empty"
    else:
        check_counter += 1

    if upwd == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    
    if check_counter == 2:
        if(uname == username and upwd == pwd):
            messagebox.showinfo('Login Status', 'Logged in Successfully!')
            
            #Close the current window
            ws.destroy()   

            #Launch the main GUI
            launch_contact_book()

            #Initiate the main contact book GUI
            #window.mainloop()
        else:
            messagebox.showerror('Login Status', 'Invalid username or password')
    else:
        messagebox.showerror('', warn) 

'''Registering an account that eventually connects to your Contact Database''' 
var = StringVar()
var.set('male')

'''References to the text file 'naStates.txt' to pass the information when registering account'''
location = []
variable = StringVar()
USA = open("naStates.txt", 'r')
for states in USA: 
    states = states.rstrip('\n')
    location.append(states)
variable.set(location[49])

################   LEFT_FRAME (Logging in)  #####################
left_frame = Frame(
    ws,
    bd = 2,
    bg = '#CCCCCC',
    relief = SOLID,
    padx = 10,
    pady = 10
)

Label(
    left_frame,
    text = "Enter Email",
    bg = '#CCCCCC',
    font = f
).grid(row = 0, column = 0, sticky = W, pady = 10)

Label(
    left_frame,
    text = "Enter Password",
    bg = '#CCCCCC',
    font = f
).grid(row = 1, column = 0, pady = 10)

email_tf = Entry(
    left_frame,
    font = f
)

pwd_tf = Entry(
    left_frame,
    font = f,
    show = '*'
)

login_btn = Button(
    left_frame,
    width = 15,
    text = 'Login',
    font = f,
    relief = SOLID,
    cursor = 'hand2',
    command = login_response
)

#################  RIGHT_FRAME(Register Account) ###########################
right_frame = Frame(
    ws,
    bd = 2,
    bg = '#CCCCCC',
    relief = SOLID,
    padx = 10,
    pady = 10
)

Label(
    right_frame,
    text = "Enter Name",
    bg = '#CCCCCC',
    font = f
).grid(row = 0, column = 0, sticky = W, pady = 10)

Label(
    right_frame,
    text = "Enter Email",
    bg = '#CCCCCC',
    font = f
).grid(row = 1, column = 0, sticky = W, pady = 10)

Label(
    right_frame,
    text = "Contact Number",
    bg = '#CCCCCC',
    font = f
).grid(row = 2, column = 0, sticky = W, pady = 10)

Label(
    right_frame,
    text = "Select Gender",
    bg = '#CCCCCC',
    font = f
).grid(row = 3, column = 0, sticky = W, pady = 10)

Label(
    right_frame,
    text = "Select State",
    bg = '#CCCCCC',
    font = f
).grid(row = 4, column = 0, sticky = W, pady = 10)

Label(
    right_frame,
    text = "Enter Password",
    bg = '#CCCCCC',
    font = f
).grid(row = 5, column = 0, sticky = W, pady = 10)

Label(
    right_frame,
    text = "Re-Enter Password",
    bg = '#CCCCCC',
    font = f
).grid(row = 6, column = 0, sticky = W, pady = 10)

gender_frame = LabelFrame(
    right_frame,
    bg = '#CCCCCC',
    padx = 10,
    pady = 10
)

#Allow User input and checks it 
register_name = Entry(
    right_frame,
    font = f
)

register_email = Entry(
    right_frame,
    font = f
)

register_mobile = Entry(
    right_frame,
    font = f
)

#Selecting Gender Code
male_rb = Radiobutton(
    gender_frame,
    text = 'Male',
    bg = '#CCCCCC',
    variable = var,
    value = 'male',
    font = ("Times", 10)
)

female_rb = Radiobutton(
    gender_frame,
    text = 'Female',
    bg = '#CCCCCC',
    variable = var,
    value = 'female',
    font = ("Times", 10)
)

others_rb = Radiobutton(
    gender_frame,
    text = 'Others',
    bg = '#CCCCCC',
    variable = var,
    value = 'others',
    font = ("Times", 10)
)

#Picking States Code
register_country = OptionMenu(
    right_frame,
    variable,
    *location
)

register_country.config(
    width = 15,
    font = ("Times", 12)
)

register_pwd = Entry(
    right_frame, 
    font = f,
    show = '*'
)

pwd_again = Entry(
    right_frame,
    font = f,
    show = '*'
)

register_btn = Button(
    right_frame,
    width = 15,
    text = 'Register',
    font = f,
    relief = SOLID,
    cursor = 'hand2',
    command = insert_record
)

##### LEFT_FRAME WIDGETS ######
email_tf.grid(row = 0, column = 1, pady = 10, padx = 20)
pwd_tf.grid(row = 1, column = 1, pady = 10, padx = 20)
login_btn.grid(row = 2, column = 1, pady = 10, padx = 20)
left_frame.place(x = 50, y = 50)

##### RIGHT_FRAME WIDGETS ########
register_name.grid(row = 0, column = 1, pady = 10, padx = 20)
register_email.grid(row = 1, column = 1, pady = 10, padx = 20)
register_mobile.grid(row = 2, column = 1, pady = 10, padx = 20)
register_country.grid(row = 4, column = 1, pady = 10, padx = 20)
register_pwd.grid(row = 5, column = 1, pady = 10, padx = 20)
pwd_again.grid(row = 6, column = 1, pady = 10, padx = 20)
register_btn.grid(row = 7, column = 1, pady = 10, padx = 20)
right_frame.place(x = 550, y = 50)

gender_frame.grid(row = 3, column = 1, pady = 10, padx = 20)
male_rb.pack(expand = True, side = LEFT)
female_rb.pack(expand = True, side =LEFT)
others_rb.pack(expand = True, side = LEFT)

#Infinite Loop
ws.mainloop()

