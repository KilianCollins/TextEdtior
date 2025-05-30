import tkinter as tk
from tkinter import ttk

def return_pressed(event):
    print('Return key pressed.')
# window is made
root = tk.Tk()
# button is made and named save
btn = ttk.Button(root, text='Save')

# '<Return>' is how the comiler listens for the return key?
# i need to know how to find all the event names so i can use them
# event bound to a button and a funciton
btn.bind('<Return>', return_pressed)

btn.focus() # what does this do? is it like the .grid() function
btn.pack(expand=True) # spacing?
root.mainloop() # end of file