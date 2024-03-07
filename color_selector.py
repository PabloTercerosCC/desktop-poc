import tkinter as tk
from tkinter import colorchooser

class ColorSelector:
    def __init__(self, on_color_selected):
        self.root = tk.Tk()
        self.root.title("Color Selector")

        self.selected_color = tk.StringVar()

        self.color_label = tk.Label(self.root, text="Selected Color", bg="white", padx=10, pady=5)
        self.color_label.pack(pady=10)

        self.choose_color_button = tk.Button(self.root, text="Choose Color", command=self.choose_color)
        self.choose_color_button.pack()

        self.color_entry = tk.Entry(self.root, textvariable=self.selected_color, state="readonly", width=30)
        self.color_entry.pack(pady=10)

        self.on_color_selected = on_color_selected

    def choose_color(self):
        color = colorchooser.askcolor(title="Select Color")
        if color[1]:  # Check if a color is chosen (user didn't cancel)
            self.selected_color.set(color[1])
            self.color_label.config(bg=color[1])
            self.on_color_selected(color[1])

    def run(self):
        self.root.mainloop()
