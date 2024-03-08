import tkinter as tk
from tkinter import ttk

def create_radio_button_frame(parent_frame):
    frame = ttk.Frame(parent_frame, padding="10")

    # Variable to hold the selected option
    option = tk.StringVar(value="Option1")

    # Radio button labels and their corresponding values
    options = [("Jungle", "Jungle"),
               ("City", "City"),
               ("Desert", "Desert"),
               ("Snow", "Snow")]

    # Create and place radio buttons
    for i, (text, value) in enumerate(options, start=1):
        radio_button = ttk.Radiobutton(frame, text=text, value=value, variable=option)
        radio_button.grid(row=i, column=0, columnspan=2, sticky=tk.W, padx=5)

    return frame, option
