# import tkinter as tk
# from tkinter import ttk
#
# def handle_event(event, msg1, msg2):
#     print(f"Event: {event}")
#     print(f"Message 1: {msg1}")
#     print(f"Message 2: {msg2}")
#
# root = tk.Tk()
# btn = ttk.Button(root, text="Click Me")
#
# # Bind Return key to btn with lambda passing event + 2 messages
# btn.bind("<Return>", lambda event : handle_event(event=event, msg1=str(dir(event)),msg2="yo"))
#
# btn.pack()
# btn.focus()
# root.mainloop()


import tkinter as tk
from tkinter import ttk

def handle_event(event, msg1, msg2, msg3):
    print(f"Event: {event}")
    print(f"Message 1: {msg1}")
    print(f"Message 2: {msg2}")
    print(f"Message 3: {msg3}")


# def triangulate_cursor():


root = tk.Tk()
btn = ttk.Button(root, text="Click Me")

# Bind Return key to btn with lambda passing event + 2 messages
btn.bind("<Return>", lambda event_obj : handle_event(event=event_obj, msg1=str(event_obj.x) + "x coord",msg2=str(event_obj.y)+"y coord", msg3=dir(event_obj)))

btn.pack()
btn.focus()
root.mainloop()
