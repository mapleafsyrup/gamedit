import tkinter
from tkinter import *
from tkinter import ttk
import os
import fileread

# Window setup
root = tkinter.Tk()
root.title("Gamedit " + open("README.md").readlines()[1])
root.geometry("600x500")
root.resizable(False, False)

# Scrollbar
# Bonus question: Which asshole made it this complicated?
frame_main = Frame(root)
frame_main.pack(fill=BOTH, expand=1)

canvas = Canvas(frame_main)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

scrollbar = ttk.Scrollbar(frame_main, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

sFrame = Frame(canvas)
canvas.create_window((0,0), window=sFrame, anchor="nw")

# Create buttons



root.mainloop()


