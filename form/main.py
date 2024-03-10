import tkinter as tk
from tkinter import ttk
from entry_module import create_name_entry_frame
from radio_button_module import create_radio_button_frame
from drop_menu_module import create_drop_menu_frame
from button_module import create_button_frame

# Create the main window
root = tk.Tk()
root.title("AntOps Form")

# Set the style to 'clam'
style = ttk.Style()
style.theme_use('clam')

# Function to create title labels
def create_title_label(parent, text, row, column=0):
    label = tk.Label(parent, text=text, font=('Helvetica', 12, 'bold'))
    label.grid(row=row, column=column, columnspan=2, pady=(10, 5), sticky=tk.W)
    return label

# Create a title label for the "Physics" entries
create_title_label(root, "Physics:", row=0)

# Create a list to store name entry frames and corresponding entry widgets
physics = ["Calibre", "Bullet weight", "Distance", "Ammo"]
name_entries_physics = []
for i in range(1, 5):
    name_entry_label = f"{physics[i-1]}:"
    name_entry_frame, name_entry = create_name_entry_frame(root, label_text=name_entry_label)
    name_entry_frame.grid(row=i, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    name_entries_physics.append((name_entry_label, name_entry))

# Create a title label for the "Environment" entries
create_title_label(root, "Environment:", row=5)

# Create a list to store name entry frames and corresponding entry widgets for "Environment"
environment = ["Temperature", "Altitude", "Pressure", "Humidity"]
name_entries_environment = []
for i in range(6, 10):
    name_entry_label = f"{environment[i-6]}:"
    name_entry_frame, name_entry = create_name_entry_frame(root, label_text=name_entry_label)
    name_entry_frame.grid(row=i, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    name_entries_environment.append((name_entry_label, name_entry))

# Create radio buttons for "Scenery"
create_title_label(root, "Scenery:", row=0, column=1)
radio_button_frame, option = create_radio_button_frame(root)
# Move Scenery to the right, aligning it with the start of Physics
radio_button_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), rowspan=4)

# Create drop-down menu for "Stress Level"
create_title_label(root, "Stress Level:", row=5, column=1)
drop_menu_frame, percentage_var = create_drop_menu_frame(root)
# Move Stress Level to the right, aligning it with the start of Environment
drop_menu_frame.grid(row=6, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), rowspan=4)

# Note: Adjusting button frame to span across both columns for aesthetic reasons, optional
button_frame = create_button_frame(root, name_entries_physics + name_entries_environment, option, percentage_var)
button_frame.grid(row=10, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

# Start the main loop
root.mainloop()
