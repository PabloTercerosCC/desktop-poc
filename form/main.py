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

# Create a list to store name entry frames and corresponding entry widgets
name_entries = []
for i in range(1, 5):
    name_entry_label = f"Name {i}:"
    name_entry_frame, name_entry = create_name_entry_frame(root, label_text=name_entry_label)
    name_entry_frame.grid(row=i - 1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    name_entries.append((name_entry_label, name_entry))

# Create frames for other modules
radio_button_frame, option = create_radio_button_frame(root)
drop_menu_frame, percentage_var = create_drop_menu_frame(root)
button_frame = create_button_frame(root, name_entries, option, percentage_var)

# Grid layout for frames
radio_button_frame.grid(row=4, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
drop_menu_frame.grid(row=5, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
button_frame.grid(row=6, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Start the main loop
root.mainloop()
