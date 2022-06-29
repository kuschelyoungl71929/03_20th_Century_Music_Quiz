#Import the required library
import tkinter as tk
from functools import partial
import random
import re

class Timer():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="", font=('Times New Roman', 40))
        self.label.pack()
        self.now = tk.IntVar()
        self.now.set(60)
        self.ok =()
        self.updatetimer()
        
        self.root.mainloop()
    
    def updatetimer(self):
        current = self.now.get()
        self.ok = (current - 1 )
        self.label.configure(text = self.ok)

        self.root.after(10000, self.updatetimer())

gui = Timer()