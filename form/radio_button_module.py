import tkinter as tk
from tkinter import ttk

def create_radio_button_frame(parent_frame):
    frame = ttk.Frame(parent_frame, padding="10")

    # Variable to hold the selected option
    option = tk.StringVar(value="Option1")

    # Radio button labels and their corresponding values
    options = [("Option1", "Option1"),
               ("Option2", "Option2"),
               ("Option3", "Option3"),
               ("Option4", "Option4")]

    # Create and place radio buttons
    for i, (text, value) in enumerate(options, start=1):
        radio_button = ttk.Radiobutton(frame, text=text, value=value, variable=option)
        radio_button.grid(row=i, column=0, columnspan=2, sticky=tk.W, padx=5)

    return frame, option
