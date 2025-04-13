import tkinter as tk
from tkinter import simpledialog,messagebox

# Ask for input
user_input = simpledialog.askstring("Input", "Enter your name: ")

print("Hello", user_input)


# Tkinter - messageBox
messagebox.showinfo("Output","Hello, Welcome!")