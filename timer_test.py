#Import the required library
from tkinter import * 
import time
class Timer():
    def __init__(self):
        self.root = Tk()
        self.label = Label(text="", font=('Times New Roman', 40))
        self.label.pack()
        self.updateClock()
        self.root.mainloop()
    def updateClock(self):
        now = time.strftime("%S")
        now = int(now)
        timer= 60 - now
        self.label.configure(text = timer)
        self.root.after(1000, self.updateClock)
gui = Timer()