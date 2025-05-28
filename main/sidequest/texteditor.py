import sys
import tkinter
from idlelib.run import exit_now
from tkinter import *
from dataclasses import InitVar
from tkinter import filedialog
from tkinter import Button, Menubutton
from tkinter import  filedialog


from numpy.f2py.auxfuncs import l_and
from pygame.event import clear

root =  tkinter.Tk("Text Editor")
# root.geometry("400x300")
# CREATES window

# root=Tk("Text Editor")

#
font_size = 12
text= tkinter.Text(root)


# text reception time
def save_as():
    global text
    # caputred text
    t = text.get("1.0", "end-1c")

#     save location
    save_location =tkinter.filedialog.asksaveasfilename(
    defaultextension=".txt",
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    title="Save As"
                                                        ) # what does this do
    # sdfa


    file_a =open(save_location, "w+") # what sort of encoding happens for w+??
    # store the text to the file just made with the text captured earlier
    file_a.write(t)
    file_a.close()

def open_file_x():
    '''later todo:
            add the ability to open and accept and make  .dox, .csv, ect. and other file types
             a check to see if file is of visula type and deny that for now '''
    # opens f
    file_name = filedialog.askopenfilename(
                                            initialdir="/",
                                            title="File Explorer",
                                            filetypes=(("Text File","*.txt"),("all files","*.*"))
                                            )
    # reads selection
    with open(file_name, "r") as file:
        # stores selceted file
        contents = file.read()
    #clears what ever what in the text wiget
    text.delete("1.0", "end")
    # inserts contents of file at line 0 colum 0
    text.insert("0.0", contents)





#     save button
#  place the button
# save_button.place(x=0,y=0)



def times_new_roman():
    global font_size
    global text
    text.config(font=("Times New Roman",font_size))

def helvetica():
    global font_size
    global text
    # text.config("Helvetica") # incorrect
    text.config(font=("Helvetica",font_size))

def courier_new():
    global font_size
    global text
    text.config(font=("Courier New",font_size))

def arial():
    global font_size
    global text
    text.config(font=("Arial",font_size))

# font button making, its a drop down list that letst the user select which font hey want

# if tkinter.Widget.i

    # font_choice.config(relief="sunken")

# goal press font button and have it stay sunken untill a menu item has been selected then it will pop bakc up to its origian astate
    # to look up    
    # bind("<Button-1>", callback) → To detect when the button is pressed.
    #
    # Menubutton.config(relief="sunken") → To simulate being pressed down.
    #
    # Menu.entryconfig() or better: just modify Menubutton.config() inside each font-change function.
    #
    # Possibly after() → To delay/reset relief if needed.

# make a button to choose and or open a file in the editor

# make button
# when pressed opens the file explorer







# what does this do?
# times_new_roman_FONT = InitVar()
# courier_new_FONT     = InitVar()
# arial_FONT           = InitVar()
# helvetica_FONT       = InitVar()

def delta_font(font):
    """*** when storing fucntions to call store wothout the () other wise key call will call it imediatly"""
    """ font refrence storeer and acessor"""
    fonts = {
            "times new roman": times_new_roman,
            "helvetica": helvetica            ,
             "courier new": courier_new
             }
    return fonts.get(font.lower())

# print(delta_font("helvetica")())


# breaks down tthe steaps of what each componnetn of theses comands do



# delta text size

# delta text color

# delta back round color

# insert pictures button

######################### buttons #####################################3
Exit_Program = tkinter.Button(root, text="Close", command=sys.exit)

    #font menu button
font_choice = tkinter.Menubutton(root, text="Font", relief="raised", borderwidth=2) # is this an  object of the Menubutton class? or an instance? are those the same thing?
font_choice.menu = tkinter.Menu(font_choice, tearoff=0) #why doesnt this work?
font_choice["menu"]= font_choice.menu
font_choice.menu.add_checkbutton(label="Courier", command=courier_new)
font_choice.menu.add_checkbutton(label="Helvetica", command=helvetica)
font_choice.menu.add_checkbutton(label="Times New Roman", command=times_new_roman)
font_choice.menu.add_checkbutton(label="Arial",command=arial)

    #save button
save_button = Button(root, text="Save As", command=save_as)

    #opens file explorer
open_file = tkinter.Button(root, text="Open File", command=open_file_x)


#


######### button placement
save_button.grid(row=0, column=0)
font_choice.grid(row=0, column=1)
open_file.grid(row=0, column=2)
Exit_Program.grid(row=0, column=9)
# all buttons must be above text.grid()
text.grid(row=1, column=0,columnspan=10)

# \/ the program stops looking for instructions after here \/
# save_button.mainloop() # this adds the button to loop # wrong objects do not have the mainloop()
root.mainloop()

