# Homemade Simple Tkinter Text Editor

A beginner-to-intermediate level **Python GUI Text Editor** built with `tkinter`, aimed to learn GUI design, event handling, and widget configuration by doing. This project replicates basic features found in common text editing programs, with additional emphasis on customization and experimentation.

---

## 📌 What This Project Is

This is a functional and expandable GUI-based **Text Editor** application. It allows users to:

- Write and edit text
- Save and open `.txt` files
- Change font types
- Change selected text colors
- Change the background color of the editor
- Use a clean, menu-driven interface for styling

It is designed to balance **functionality** with **learning-by-doing**, using clear code and custom features to explore event-driven GUI programming in Python.

--- 

## 🎯 Why This Project Exists

This project was created with one primary goal in mind:

> **"To learn how GUI frameworks like `tkinter` actually work by building something non-trivial from scratch."**

Instead of copying tutorials line-by-line, this project encourages:
- Deep experimentation with widgets, geometry managers, events, and binding
- Solving real design problems (menus, user input, error handling)
- Understanding through implementation

---

## 🧠 Developer Goals (Learning Objectives)

- [x] Understand the `tkinter` layout and widget system
- [x] Handle text input/output in GUI applications
- [x] Capture and apply styles (fonts, colors) dynamically
- [x] Bind events like mouse clicks and selections
- [x] Use `lambda` functions for widget commands
- [ ] Add error handling and file format filtering
- [ ] Add support for additional file formats (.docx, .csv, etc.)
- [ ] Allow for custom font sizes and styles
- [ ] Add image insertion and file preview
- [ ] Package this app with `pyinstaller` or similar
- [ ] Add dynamic Dark and Light "Theme" or "Mode"
- [ ] Create Insert tables and or graphs that the application generates based on input

---

## ✅ Features Implemented So Far

- [x] Save file as `.txt`
- [x] Open `.txt` files
- [x] Change selected font (Times New Roman, Courier, etc.)
- [x] Change selected text color (Red, Blue, etc.) -- inprogress
- [x] Change background color (White, Gray, etc.) -- inprogress
- [x] Use menu buttons for styling options
- [x] Dynamic tagging of selected text (using `.tag_add` and `.tag_config`)
- [x] Use of lambda functions in GUI actions
- [x] Button state toggling (raised ↔ sunken)

## Features To Be Added:
- [o] Store changes made by user to text color, and background color so that the changes "stick" to the document so that they remain once saved and apear when the file is opened.
- [o] Prettier formating: add a margin around text so the text apears less "crushed" or "cramped"
- [o] Paragraph breaks and bias: shift left, right or middle just like in ggl docs
- [o] Add more fonts
- [o] Insert Images

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **GUI Library:** `tkinter`
- **Other Libraries:**
  - `random` (for unique tag names)
  - `sys` (for program exit)
  - `filedialog` (for file selection dialogs)
  - `tkinter` (for GUI and visuals)

---

## 📝 How to Run

1. Make sure you have Python 3.10+ installed.
2. Run the program with:

   ```bash
   python your_file_name.py
