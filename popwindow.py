import sys
#import contacts.py
import tkinter as tk


#title opening page when launched goes right
window = tk.Tk()

window.title('Contact Book')

label = tk.Label(
window,
text = "Welcome",
background = "white",
foreground = "black",
width = 2000,
height = 2000
).place(x=25,y=50)

#buttons for functions will be going here
addContactButton = tk.Button(
    window,
    text = "Add Contact",
    width = 30,
    height = 30,
    background = "blue",
    foreground = "black"    
)

#button for delCont
delContactButton = tk.Button(
    window,
    text = "Delete Contact",
    width = 30,
    height = 30,
    background = "red",
    foreground = "black"    
)

#button for modCont
modContactButton = tk.Button(
    window,
    text = "Modify Contact",
    width = 30,
    height = 75,
    background = "yellow",
    foreground = "black"    
)

delContactButton.pack()
addContactButton.pack()
modContactButton.pack()
delContactButton.flash()
addContactButton.flash()
modContactButton.flash()


#launches/runs the windowke
window.mainloop()