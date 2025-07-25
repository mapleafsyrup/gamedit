import tkinter
from tkinter import *

# window setup
root = tkinter.Tk()
root.title("Gamedit " + open("README.md").readlines()[1])
root.geometry("600x500")
root.resizable(False, False)

root.mainloop()
