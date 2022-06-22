from tkinter import * 
from functools import partial
import re

class Start:
    def __init__(self, partner):
       
        # Bkg Variable
        start_bkg = "#BAC8D3"

        # Main Window
        self.start_frame = Frame(width=240, height=150, bg=start_bkg, padx=10, pady=15)
        
        self.start_frame.grid()
        
        #title
        self.start_label = Label(self.start_frame, text = "Music of the \n 20th Century", font="garamond 20 bold", justify=LEFT, bg=start_bkg)
        self.start_label.grid(row=0, sticky=NW)
        #button frame
        self.button_frame = Frame(self.start_frame, width = 200, height = 100, bg = start_bkg, pady =10)
        self.button_frame.grid(column=0, row=1, padx=(0,0))

        #start button
        self.start_button = Button(self.button_frame,text = "Start", width = 20, height = 1 ,font="garamond 14" , background="#B0E3E6")
        self.start_button.grid(row = 0, column = 0, padx=(150,0))
        #spacer
        self.start_label = Label(self.button_frame, text = "", font="garamond 19 bold", wrap=250, justify=LEFT, bg=start_bkg, pady=1)
        self.start_label.grid(row=1)
        #info button
        self.i_button = Button(self.button_frame, text = "i",font="Arial 10 bold", height = 1, width = 2, bg="#ADC9ED")
        self.i_button.grid(row=1, sticky = W)  
        #mode button
        self.exit_button = Button(self.button_frame,text= "Exit", width = 20, height = 1 ,font="garamond 14", background="#9CE0ED")
        self.exit_button.grid(row = 2, column = 0)
        
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    something = Start(root)
    root.mainloop()