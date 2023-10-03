import json
import os
import sqlite3 
import sys
from tkinter import *
from tkinter import messagebox
from contacts import Contacts

#Designing Main Screen So, first of all, you have to design the main screen.
#two buttons Login and Register.

database = Contacts()

def onClick():
    messagebox.showinfo("Information", "There is no database yet")

mainscreen = Tk()   # create a GUI window 
mainscreen.geometry("800x800") # set the configuration of GUI window 
mainscreen.title(" Login Page") # set the title of GUI window

#creating a database

# create a Form label 
Label(text="Login Window Example", bg="blue", width="30", height="2", font=("Calibri", 13)).pack() 
Label(text="").pack() 

# create Login Button 
enterDateBase = Button(text="Login", command=onClick,  height="2", width="30").pack() 
Label(text="").pack() 


# create a register button
createDataBase = Button(text="Register", height="2",width="30").pack() #add later ==> command = database.set_database_name).pack()
 
mainscreen.mainloop() # start the GUI

