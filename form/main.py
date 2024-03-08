import tkinter as tk
from tkinter import ttk
from entry_module import create_name_entry_frame
from radio_button_module import create_radio_button_frame
from drop_menu_module import create_drop_menu_frame
from button_module import create_button_frame

# Create the main window
root = tk.Tk()
root.title("Name Form with Options and Percentage")

# Set the style to 'clam'
style = ttk.Style()
style.theme_use('clam')

# Function to create title labels
def create_title_label(parent, text, row):
    label = tk.Label(parent, text=text, font=('Helvetica', 12, 'bold'))
    label.grid(row=row, column=0, columnspan=2, pady=(10, 5), sticky=tk.W)
    return label

# Create a title label for the entries
create_title_label(root, "Physics:", row=0)

# Create a list to store name entry frames and corresponding entry widgets
physics = ["calibre", "bullet weight", "distance", "ammo"]
name_entries = []
for i in range(1, 5):
    name_entry_label = f"{physics[i-1]}:"
    name_entry_frame, name_entry = create_name_entry_frame(root, label_text=name_entry_label)
    name_entry_frame.grid(row=i, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    name_entries.append((name_entry_label, name_entry))

# Create radio buttons
create_title_label(root, "Scenary:", row=5)
radio_button_frame, option = create_radio_button_frame(root)
radio_button_frame.grid(row=6, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create drop down menu
create_title_label(root, "Stress Level:", row=7)
drop_menu_frame, percentage_var = create_drop_menu_frame(root)
drop_menu_frame.grid(row=8, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create button
button_frame = create_button_frame(root, name_entries, option, percentage_var)
button_frame.grid(row=9, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Start the main loop
root.mainloop()
