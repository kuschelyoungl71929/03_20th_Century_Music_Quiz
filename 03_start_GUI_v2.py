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
        self.start_button = Button(self.button_frame,text = "Start", width = 20, height = 1 ,font="garamond 14" , background="#B0E3E6", command = self.ten_quiz)
        self.start_button.grid(row = 0, column = 0, padx=(200,0))
        #spacer
        self.start_label = Label(self.button_frame, text = "", font="garamond 19 bold", wrap=250, justify=LEFT, bg=start_bkg, pady=1)
        self.start_label.grid(row=1)
        #info button
        self.i_button = Button(self.button_frame, text = "i", font="Arial 10 bold", height = 1, width = 2, command=self.info)
        self.i_button.grid(row=1, sticky = W)
        #mode button
        self.mode_button = Button(self.button_frame,text= "Mode Select", width = 20, height = 1 ,font="garamond 14", background="#9CE0ED")
        self.mode_button.grid(row = 2, column = 0)

    def info(self):  
        print("help")
        get_help = Info(self)
        get_help.help_text.configure(text="Help text")

    def ten_quiz(self):
        print("start")
        get_game = Quiz_10(self) 
        root.withdraw()

class Info: 
    def __init__(self, partner): 

        #background colour
        bkg_colour= "#B0E3E6"

        #Button off
        partner.i_button.config(state=DISABLED)

        #opens a new window
        self.i_box = Toplevel()

        #GUI Frame
        self.i_frame = Frame(self.i_box, width=400, height=300, bg=bkg_colour, padx=10, pady=10)
        
        self.i_frame.grid()

        #Help Heading 0
        self.i_label = Label(self.i_frame, text="Information", font=("Garamond 19 bold"), bg=bkg_colour, padx=10, pady=15)
       
        self.i_label.grid(row=0)

        #Help Text 1 
        self.i_text = Label(self.i_frame, text="Lorem ipsum \ndolor sit amet,\n consectetur adipiscing elit, \nsed do eiusmod \ntempor incididunt ut \nlabore et dolore \nmagna aliqua.", font = "Verdana 9", width = 22, justify=LEFT, bg="#9CE0ED" , wrap=250,  borderwidth=1 , relief=SOLID)
        self.i_text.grid(row=1)

        #Dismiss button 2 
        self.dismiss_button = Button(self.i_frame, text="Exit", width=10,font="garamond 12", command=partial(self.close_button, partner))
        self.dismiss_button.grid(row=2,pady=10)
    
    #close help function
    def close_button(self, partner):
        partner.i_button.config(state=NORMAL)
        self.i_box.destroy()
  
class Quiz_10:
    def __init__(self, partner):
        
        partner.start_button.config(state=DISABLED)

        self.quiz_10_box = Toplevel()
        
        self.quiz_10_box.protocol('WM_DELETE_WINDOW', partial(self.close_button, partner))
        
        self.quiz_10_frame = Frame(self.quiz_10_box, width=400, height=300, bg="#B1DDF0",padx=10, pady=10) 
   
    def close_button(self, partner):
        partner.start_button.config(state=NORMAL)
        self.quiz_10_box.destroy()
        root.deiconify()
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    something = Start(root)
    root.mainloop()