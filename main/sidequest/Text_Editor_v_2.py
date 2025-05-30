import random
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
root.configure(background="white")

# root.geometry("400x300")
# CREATES window

# root=Tk("Text Editor")

#
font_size = 12
background_color = "White"
text= tkinter.Text(root)
menu_state = "raised"


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


# when the menu button is pressed i want the main button(the one that contains all the small ones) to become depressed ((sunken))

# main B remains sunken untill user clicks off or selects a sub button (one of the small ones)

def menu_sunken(event):
    global menu_state
    font_choice.config(relief="sunken")
    print("sunken")
def menu_raise(event):
    font_choice.config(relief="raised")
    print("raised")



# what does this do?
# times_new_roman_FONT = InitVar()
# courier_new_FONT     = InitVar()
# arial_FONT           = InitVar()
# helvetica_FONT       = InitVar()

def delta_font(font=("Times New Roman", font_size)):
    font_choice.config(relief="sunken")
    tag_name_current = "n" + str(random.randint(0, 50))
    tag_name_previous = tag_name_current
    tag_name = "n" + str(
        random.randint(0, 50)) if tag_name_previous != tag_name_current else "t" + str(random.randint(50, 990)
                        )


    try:
        current_pos_of_cursor = text.index(tkinter.INSERT)
        highlight_start = text.index(tkinter.SEL_FIRST)
        highlight_stop = text.index(tkinter.SEL_LAST)
        text.tag_add(tag_name, highlight_start, highlight_stop)
        text.tag_config(tag_name, font=font)

    except tkinter.TclError:
        print("nothing selected")

def delta_color_text(color:str= "black"):
    '''i tied this functionallity to a button bc idk how eles to get this to not crash '''
    tag_name_current = "t" + str(random.randint(0, 50))
    tag_name_previous = tag_name_current
    tag_name = "t" + str(
        random.randint(0, 50)) if tag_name_previous != tag_name_current else "t" + str(random.randint(50, 990)
                        )
    # global highlight_start, highlight_stop
    try:
        current_pos_of_cursor = text.index(tkinter.INSERT)
        highlight_start = text.index(tkinter.SEL_FIRST)
        highlight_stop = text.index(tkinter.SEL_LAST)
        text.tag_add(tag_name, highlight_start, highlight_stop)
        text.tag_config(tag_name, foreground=color)

    except tkinter.TclError:
        print("nothing selected")

def delta_bg_color(color:str="white"):
    text.configure(background=color)

def open_font_menu(event):
    font_choice.config(relief="sunken")
    # font_choice.event_generate('<Button-1>')
def raise_font_menu(event):
    font_choice.config(relief="raised")

# def wait()

# bg color button
bg_color_button = tkinter.Menubutton(root,text="Backround Color", relief="raised",borderwidth=2)
bg_color_button.menu = tkinter.Menu(bg_color_button,tearoff=0)
bg_color_button["menu"] = bg_color_button.menu
#  there has got to be a better more efficient way than this boilerplate ridiculousness
bg_color_button.menu.add_command(label="White",command=lambda:delta_bg_color("white"))
bg_color_button.menu.add_command(label="Gray",command=lambda:delta_bg_color("gray"))
bg_color_button.menu.add_command(label="Black",command=lambda:delta_bg_color("black"))
bg_color_button.menu.add_command(label="Blue",command=lambda:delta_bg_color("blue"))
bg_color_button.menu.add_command(label="Green",command=lambda:delta_bg_color("green"))
bg_color_button.menu.add_command(label="Yellow",command=lambda:delta_bg_color("yellow"))
bg_color_button.menu.add_command(label="Orange",command=lambda:delta_bg_color("orange"))
bg_color_button.menu.add_command(label="Red",command=lambda:delta_bg_color("red"))
bg_color_button.menu.add_command(label="Pink",command=lambda:delta_bg_color("pink"))
bg_color_button.menu.add_command(label="White",command=lambda:delta_bg_color("white"))








# def delt_text_size(font_size:int=12):
#     tag_name_current = "s" + str(random.randint(0, 50))
#     tag_name_previous = tag_name_current
#     tag_name = "s" + str(
#         random.randint(0, 50)) if tag_name_previous != tag_name_current else "s" + str(random.randint(50, 990)
#                                                                                        )
#     # global highlight_start, highlight_stop
#     try:
#         current_pos_of_cursor = text.index(tkinter.INSERT)
#         highlight_start = text.index(tkinter.SEL_FIRST)
#         highlight_stop = text.index(tkinter.SEL_LAST)
#         text.tag_add(tag_name, highlight_start, highlight_stop)
#         text.tag_config(tag_name, )
#
#     except tkinter.TclError:
#         print("nothing selected")


# breaks down tthe steaps of what each componnetn of theses comands do

# delta text size

# delta text color

# delta back round color

# insert pictures button

######################### buttons #####################################3


    #font menu button
font_choice = tkinter.Menubutton(root, text="Font", relief="raised", borderwidth=2) # is this an  object of the Menubutton class? or an instance? are those the same thing?
font_choice.menu = tkinter.Menu(font_choice, tearoff=0) #why doesnt this work?
font_choice["menu"]= font_choice.menu
# man the lambda function is really powerful, i still dont quite understand how it works
                                                                #i did the list so that the lambda can accept multipl
                                                                # statments bc i want the buttin to raise then lower after a menu item has been selected
font_choice.menu.add_command(label="Courier", command=lambda:[delta_font(font=("Courier New", font_size)), raise_font_menu])
font_choice.menu.add_command(label="Helvetica", command=lambda:[delta_font(font=("Helvetica", font_size)), raise_font_menu])
font_choice.menu.add_command(label="Times New Roman", command=lambda:[delta_font(font=("Times New Roman", font_size)), raise_font_menu] )
font_choice.menu.add_command(label="Arial",command=lambda:[delta_font(font=("Arial",font_size)), raise_font_menu] )

# sinks the button on CLICK

# font_choice.bind('<ButtonPress-1>',(raise_font_menu if font_choice.event_info('<ButtonRelease-1>') else open_font_menu) )
font_choice.bind('<ButtonPress-1>',open_font_menu)

# font_choice.bind("ButtonPress-1", lambda e: menu_sunken(event=e))
# root.update_idletasks()
# raises the button on select
# font_choice.bind("ButtonRelease-1",lambda e: menu_raise(event=e))



    #exit button
Exit_Program = tkinter.Button(root, text="Close", command=sys.exit)
    #color menu button
color_selected_text = tkinter.Menubutton(root, text="Color_Text",relief="raised",borderwidth=2)
color_selected_text.menu = tkinter.Menu(color_selected_text, tearoff=0)
color_selected_text["menu"]= color_selected_text.menu
# IT WORKS LETS GOOOOOO
# are these listed colors all the available colors?
color_selected_text.menu.add_command(label="Black", command=lambda: delta_color_text("black"))
color_selected_text.menu.add_command(label="Red", command=lambda: delta_color_text("red"))
color_selected_text.menu.add_command(label="Blue", command=lambda: delta_color_text("blue"))
                                                            # we do this way for the funciton ref bc funct needs parameters and for some reason can jusrt enter in the assingment therr
color_selected_text.menu.add_command(label="Green", command=lambda: delta_color_text("green"))
color_selected_text.menu.add_command(label="Yellow", command=lambda: delta_color_text("yellow"))
color_selected_text.menu.add_command(label="Orange", command=lambda: delta_color_text("orange"))
color_selected_text.menu.add_command(label="Pink", command=lambda: delta_color_text("pink"))
color_selected_text.menu.add_command(label="Gray", command=lambda: delta_color_text("gray"))
color_selected_text.menu.add_command(label="White",command=lambda :delta_color_text("white"))
    #save button
save_button = Button(root, text="Save As", command=save_as)

    #opens file explorer                                # we do this way for the function ref bc no parameters are needed
open_file = tkinter.Button(root, text="Open File", command=open_file_x)

#
# how do i get this to wait and only run when user has actallu selected the text



# text.pack(expand=1, fill=BOTH)

######### button placement
save_button.grid(row=0, column=0)
font_choice.grid(row=0, column=1)
open_file.grid(row=0, column=2)
color_selected_text.grid(row=0,column=3)
bg_color_button.grid(row=0, column=4)
Exit_Program.grid(row=0, column=9)
# all buttons must be above text.grid()
text.grid(row=1, column=0,columnspan=10)



# color_text(start=highlight_start, stop=highlight_stop, color="green")



# \/ the program stops looking for instructions after here \/
# save_button.mainloop() # this adds the button to loop # wrong objects do not have the mainloop()
root.mainloop()

