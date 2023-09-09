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
    width = 150,
    height = 55,
    background = "blue",
    foreground = "black"    
)

addContactButton.pack()




window.mainloop()