import tkinter as tk
from tkinter import ttk

def create_name_entry_frame(parent_frame):
    frame = ttk.Frame(parent_frame, padding="10")

    # Create a label for the name entry
    name_label = ttk.Label(frame, text="Enter your name:")
    name_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

    # Create an entry widget for the name
    name_entry = ttk.Entry(frame, width=15)
    name_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
    name_entry.focus()  # Places cursor in the name_entry widget

    return frame, name_entry
