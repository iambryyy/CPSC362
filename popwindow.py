import tkinter as tk

#title opening page when launched goes right
window = tk.Tk()

label = tk.Label(
window,
text = "Contact Book",
background = "white",
foreground = "black",
width = 2000,
height = 2000
)

#buttons for functions will be going here
addContactButton = tk.Button(
    window,
    text = "Add Contact",
    width = 250,
    height = 50,
    background = "green",
    foreground = "black"    
)




window.mainloop()