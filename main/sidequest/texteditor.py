import tkinter, tkinter.filedialog
from dataclasses import InitVar
from tkinter import Button, Menubutton

from numpy.f2py.auxfuncs import l_and

root =  tkinter.Tk("Text Editor")
# root.geometry("400x300")
# CREATES window

# root=Tk("Text Editor")

#
font_size = 12
text= tkinter.Text(root)
text.grid()

# text reception time
def save_as():
    global text
    # caputred text
    t = text.get("1.0", "end-1c")

#     save location
    save_location =tkinter.filedialog.asksaveasfilename() # what does this do
    file_a =open(save_location, "w+") # what sort of encoding happens for w+??
    # store the text to the file just made with the text captured earlier
    file_a.write(t)
    file_a.close()

#     save button
save_button = Button(root, text="Save As", command=save_as)
save_button.grid()
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

def courier_new()->str:
    global font_size
    global text
    text.config(font=("Courier New",font_size))

def arial():
    global font_size
    global text
    text.config(font=("Arial",font_size))

# font button making, its a drop down list that letst the user select which font hey want
font_choice = tkinter.Menubutton(root, text="Font")
font_choice.grid(row=0, column=0)
font_choice.menu = tkinter.Menu(font_choice, tearoff=0) #why doesnt this work?
font_choice["menu"]= font_choice.menu

# what does this do?
# times_new_roman_FONT = InitVar()
# courier_new_FONT     = InitVar()
# arial_FONT           = InitVar()
# helvetica_FONT       = InitVar()

def delta_font(font):
    """*** when storing fucntions to call store wothout the () other wise key call will call it imediatly"""
    """ font refrence storeer and acessor"""
    fonts = {
            "times new roman": times_new_roman
             ,"helvetica": helvetica
             ,"courier new": courier_new
             }
    return fonts.get(font.lower())

# print(delta_font("helvetica")())


# breaks down tthe steaps of what each componnetn of theses comands do
font_choice.menu.add_checkbutton(label="Courier", command=courier_new)
font_choice.menu.add_checkbutton(label="Helvetica", command=helvetica)
font_choice.menu.add_checkbutton(label="Times New Roman", command=times_new_roman )



# delta text size

# delta text color

# delta back round color

# insert pictures button

#








# \/ the program stops looking for instructions after here \/
# save_button.mainloop() # this adds the button to loop # wrong objects do not have the mainloop()
root.mainloop()

