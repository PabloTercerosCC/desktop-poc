import tkinter as tk
from tkinter import ttk

def create_button_frame(parent_frame, name_entry, option, percentage_var):
    frame = ttk.Frame(parent_frame, padding="10")

    # Function to be called when the submit button is clicked
    def submit_form():
        name = name_entry.get()  # Retrieves text from name_entry
        selected_option = option.get()  # Retrieves the selected option
        selected_percentage = percentage_var.get()  # Retrieves the selected percentage
        print("Name:", name)
        print("Selected Option:", selected_option)
        print("Selected Percentage:", selected_percentage)

    # Create a submit button
    submit_button = ttk.Button(frame, text="Submit", command=submit_form)
    submit_button.grid(row=0, column=0, columnspan=2, pady=5)

    return frame
