import tkinter as tk

def show_event_details(event):
    print(f"Event: {event.type}, Widget: {event.widget}, Keysym: {getattr(event, 'keysym', '')}, Button: {getattr(event, 'num', '')}, Coordinates: ({event.x}, {event.y})")

root = tk.Tk()
root.title("Event Explorer")
root.geometry("400x200")

label = tk.Label(root, text="Press any key or click the mouse inside this window", font=("Arial", 12))
label.pack(pady=40)

# Bind to general events
root.bind_all("<Key>", show_event_details)            # Any key
root.bind_all("<Button>", show_event_details)         # Any mouse button
root.bind_all("<Motion>", show_event_details)         # Mouse movement
root.bind_all("<Enter>", show_event_details)          # Mouse enters widget
root.bind_all("<Leave>", show_event_details)          # Mouse leaves widget
root.bind_all("<FocusIn>", show_event_details)        # Widget gains focus
root.bind_all("<FocusOut>", show_event_details)       # Widget loses focus

root.mainloop()
