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

# Create frames for each module
name_entry_frame, name_entry = create_name_entry_frame(root)
radio_button_frame, option = create_radio_button_frame(root)
drop_menu_frame, percentage_var = create_drop_menu_frame(root)
button_frame = create_button_frame(root, name_entry, option, percentage_var)

# Grid layout for frames
name_entry_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
radio_button_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
drop_menu_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
button_frame.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Start the main loop
root.mainloop()
