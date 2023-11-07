#import sys
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
)

#buttons for functions will be going here
addContactButton = tk.Button(
    window,
    text = "Add Contact",
    width = 30,
    height = 20,
    background = "blue",
    foreground = "black"    
)

#button for delCont
delContactButton = tk.Button(
    window,
    text = "Delete Contact",
    width = 30,
    height = 20,
    background = "red",
    foreground = "black"    
)

#button for modCont
modContactButton = tk.Button(
    window,
    text = "Modify Contact",
    width = 30,
    height = 20,
    background = "yellow",
    foreground = "black"
)

#separator for contact list that will appear on the right hand side
#window.add_separator()
#TSeparator = tk.SEPARATOR(window)
#TSeparator.config(orient = 'vertical')
#TSeparator.place(relx=.5, rely=0, relwidth=1, relheight=1)
#separator = tk.SEPARATOR(window, orient='vertical').pack(fill = Y, expand = TRUE)
#separator.place(relx=.5, rely=0, relwidth=1, relheight = 1)

#placements for the buttons to make them look more uniform
delContactButton.place(x=0, y=0)
modContactButton.place(x=210,y=0)
addContactButton.place(x=410,y=0)

#the buttons will resize and respond accordingly when resizing the pop window
delContactButton.pack(fill=tk.BOTH,side=tk.LEFT, expand=True)
modContactButton.pack(fill=tk.BOTH,side=tk.LEFT, expand=True)
addContactButton.pack(fill=tk.BOTH,side=tk.LEFT, expand=True)

#launches/runs the window
window.mainloop()