from re import A
from tkinter import * 
from functools import partial
import random

class Start:
    def __init__(self, partner):
       
        # Bkg Variable
        start_bkg = "#BAC8D3"

        # Main Window
        self.start_frame = Frame(width=240, height=150, bg=start_bkg, padx=10, pady=15)
        
        self.start_frame.grid()
        #self.start_frame.resizable(False,False)
        
        #title
        self.start_label = Label(self.start_frame, text = "Music of the \n 20th Century", font="garamond 20 bold", justify=LEFT, bg=start_bkg)
        self.start_label.grid(row=0, sticky=NW)
        #button frame
        self.button_frame = Frame(self.start_frame, width = 200, height = 100, bg = start_bkg, pady =10)
        self.button_frame.grid(column=0, row=1, padx=(0,0))

        #start button
        self.start_button = Button(self.button_frame,text = "Start", width = 20, height = 1 ,font="garamond 14" , background="#B0E3E6", command = self.mode)
        self.start_button.grid(row = 0, column = 0, padx=(150,0))
        #spacer
        self.start_label = Label(self.button_frame, text = "", font="garamond 19 bold", wrap=250, justify=LEFT, bg=start_bkg, pady=1)
        self.start_label.grid(row=1)
        #info button
        self.i_button = Button(self.button_frame, text = "i", font="Arial 10 bold", height = 1, width = 2, command=self.info)
        self.i_button.grid(row=1, sticky = W)
        #mode button
        self.exit_button = Button(self.button_frame,text= "Exit", width = 20, height = 1 ,font="garamond 14", background="#9CE0ED", command = self.exit)
        self.exit_button.grid(row = 2, column = 0)

    def exit(self):
        root.destroy()    

    def info(self):  
        print("help")
        get_help = Info(self)
     

    def ten_quiz(self):
        print("start")
        get_game = Quiz_10(self) 
        root.withdraw()
    def mode(self):
        print("mode select")
        get_game = Mode(self) 
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
        #set the button to work again
        partner.i_button.config(state=NORMAL)
        #destory the currently open box
        self.i_box.destroy()

class Mode:
    def __init__(self, partner):
        mode_bkg = "#B0E3E6"
        #opens a new window
        self.mode_box = Toplevel()
        #makes the X button in the corner functional
        self.mode_box.protocol('WM_DELETE_WINDOW', partial(self.close_button, partner))
        #frame to hold non-buttons
        self.mode_frame = Frame(self.mode_box, width = 240, height = 150, bg=mode_bkg)
        self.mode_frame.grid()
        #frame to hold buttons
        self.mode_frame_b = Frame(self.mode_frame,bg=mode_bkg, padx = 10, pady=10) 
        self.mode_frame_b.grid(row = 1, column = 0, padx=(0,240))
        
        self.title_frame = Frame(self.mode_frame, bg = mode_bkg, height = 10, width = 10)
        self.title_frame.grid(row=0)
        #title
        self.start_label = Label(self.title_frame, text = "Mode Select", font="garamond 20 bold", justify=LEFT, bg=mode_bkg)
        self.start_label.grid(row=0,column = 0,sticky=N, pady=(10,0))
        #10 questions
        self.fs_button = Button(self.mode_frame_b,text = "Freeplay 10 Questions", width = 20, height = 1 ,font="garamond 14" , background="#FFFF88", command =lambda: self.info_disp(1))
        self.fs_button.grid(row = 2, column = 0,  pady=(20,0))
        self.fl_button = Button(self.mode_frame_b,text = "Freeplay 20 Questions", width = 20, height = 1 ,font="garamond 14" , background="#CCE5FF", command =lambda:  self.info_disp(2))
        self.fl_button.grid(row = 3, column = 0,  pady=(15,0))
        self.ti_button = Button(self.mode_frame_b,text = "Timed", width = 20, height = 1 ,font="garamond 14" , background="#CDEB8B", command =lambda:  self.info_disp(3))
        self.ti_button.grid(row = 4, column = 0, pady=(15,0))
        self.mode_text = Label(self.mode_frame, text="Welcome! \nchoose a mode \nto start.", font = "Verdana 9", width = 15, justify=LEFT, bg="#9CE0ED" ,  borderwidth=1 , relief=SOLID, pady =10, padx = 15)
        self.mode_text.grid(column = 0, row=1,padx=(240,0), pady = (30,10))
        #info button
        self.i_button = Button(self.title_frame, text = "i", font="Arial 10 bold", height = 1, width = 2, command=self.info)
        self.i_button.grid(row = 0,column = 1, padx=(10,0))


    def info_disp(self, mode):
    
        mode = int(mode)

        if mode == 1:
            modetext = "A short, 10 question \nquiz with no \ntimer, you will be \nplayed short \naudio clips and \nasked to guess \nthe song they are \nfrom."
        elif mode == 2:
            modetext = "A longer, 20 question \nquiz with no \ntimer, you will be \nplayed short \naudio clips and \nasked to guess \nthe song they are \nfrom."
        else: 
            mode == 3
            modetext = "You will \nget 1 minute\nto answer as \nmany questions \nas you can,\nthe questions will ask\nyou to match\nthe lyrics to \nthe song they're from"

        self.mode_text.config(text=modetext)

        self.continue_button = Button(self.mode_frame, text = "Continue",font="Verdana 9", background="#9CE0ED", command =lambda:  self.ten_quiz(mode))
        self.continue_button.grid(column = 0, row=2,padx=(240,0), pady = (0,10))
    def ten_quiz(self, mode):

        if mode <= 2:
            Quiz_10(self, mode) 
        else:
            mode == 3
            Quiz_timed(self,mode)
        root.withdraw()
        self.mode_box.destroy()

    def timed_quiz(self,mode):

        Quiz_timed(self, mode) 
        root.withdraw()
        self.mode_box.destroy()
    def close_button(self, partner):
        #destroy the currently open box
        self.mode_box.destroy()
        #bring back the root box
        root.deiconify()
    def info(self):  

        get_help = Info(self)

class Quiz_timed:
    def __init__(self, mode, partner):
        print(mode)
        self.test =IntVar()
       
        self.test.set(mode)
        self.right_count = 0
        self.wrong_count = 0
        #opens a new window
        self.quiz_timed_box = Toplevel()
        #makes the X button in the corner functional
        self.quiz_timed_box.protocol('WM_DELETE_WINDOW', partial(self.close_button, partner))
        #frame to hold components
        self.answer_frame = Frame(self.quiz_timed_box, width=400, height= 200, bg = "#B1DDF0")
        self.answer_frame.grid(row=0, column = 0)
        self.counter = Label(self.answer_frame, text="", font = "garamond 14", bg ="#B1DDF0" )
        self.counter.grid(row = 0, sticky=NW)
        self.countdown(5)
        self.question = Label(self.answer_frame, text= "?",  font = "garamond 14", bg ="#B1DDF0" )
        self.question.grid(row=1, column = 0)
        self.a1=Button(self.answer_frame,text = "", width = 10, height = 1 ,font="garamond 13" , background="#CDEB8B", command= lambda: [self.question_rng(partner)])
        self.a1.grid(row = 2, column = 0, padx=10, pady=10)
        self.a2 = Button(self.answer_frame,text = "", width = 10, height = 1 ,font="garamond 13" ,background="#CDEB8B", command= lambda: [self.question_rng(partner)])
        self.a2.grid(row = 3, column = 0, padx=10, pady=10)
        self.a3 = Button(self.answer_frame,text = "", width = 10, height = 1 ,font="garamond 13" , background="#CDEB8B", command= lambda: [self.question_rng(partner)])
        self.a3.grid(row = 2, column = 1,  padx=10, pady=10)
        self.a4=Button(self.answer_frame,text = "", width = 10, height = 1 ,font="garamond 13" , background="#CDEB8B", command= lambda: [self.question_rng(partner)])
        self.a4.grid(row = 3, column = 1,  padx=10, pady=10) 
        self.question_rng(partner,)

    

    def question_rng(self, partner ):
        
        #set up list to hold questions
        self.a1.configure(text = '',command= lambda: [self.question_rng(partner), self.answerwrong()])
        self.a2.configure(text = '',command= lambda: [self.question_rng(partner), self.answerwrong()])
        self.a3.configure(text ='',command= lambda: [self.question_rng(partner), self.answerwrong()])
        self.a4.configure(text = '',command= lambda: [self.question_rng(partner), self.answerwrong()])
        questions = [["what colour \nis the sky?", "blue"],["1+1=?","2"],["what number \ncomes after 4?","5"],["who is the \nprime minister of \nNew Zealand(2022)?","Jacinda \nArdern"], ["why did \nthe chicken \ncross the road?", "to get to the\n other side"]]
        random.shuffle(questions)
        self.a1.configure(text = questions[1][1])
        self.a2.configure(text = questions[2][1])
        self.a3.configure(text = questions[3][1])
        self.a4.configure(text = questions[4][1])
        randomizer = random.randint(1,4)
        if randomizer == 1:
            self.a1.configure(text = questions[0][1], command= lambda: [self.question_rng(partner,), self.answerright()])

        elif randomizer == 2:
            self.a2.configure(text = questions[0][1], command= lambda: [self.question_rng(partner, ), self.answerright()])
          
        elif randomizer == 3:
            self.a3.configure(text = questions[0][1], command= lambda: [self.question_rng(partner, ), self.answerright()])
    
        elif randomizer == 4:
            self.a4.configure(text = questions[0][1], command= lambda: [self.question_rng(partner, ), self.answerright()])
        
        self.question.configure(text = questions[0][0])

        
        


    def countdown(self, count):
        self.counter.configure(text = count)
        self.counter.grid(row = 1, column = 1)
        
        if count > 0:
        
            root.after(1000, self.countdown, count-1)
        else: 
            self.to_export(self)
            self.quiz_timed_box.destroy()
        

    def close_button(self, partner):
        #destory the currently open box
        self.quiz_timed_box.destroy()
        #bring back the root box
        root.deiconify()
    def answerwrong(self):
        print("answer wrong")
        self.wrong_count +=1
        print("Questions wrong: {}".format(self.wrong_count))
        
         
    def answerright(self):
        print("answer right")
        self.right_count += 1
        
        print(self.right_count)
    def to_export(self, partner):
        
        get_end = EndScreen(self)

class EndScreen:
    def __init__(self, partner): 
        
        #background colour
        bkg_colour= "#F8CECC"
        #opens a new window
        self.endscreen_box = Toplevel()

        #GUI Frame
        self.endscreen_frame = Frame(self.endscreen_box, width=400, height=300, bg=bkg_colour, padx=10, pady=10)
        
        self.endscreen_frame.grid()

        #Help Heading 0
        self.endscreen_label = Label(self.endscreen_frame, text="", font=("Garamond 19 bold"), bg=bkg_colour, padx=10, pady=15)
       
        #Help Text 1 
        self.endscreen_text = Label(self.endscreen_frame, text="Lorem ipsum \ndolor sit amet,\n consectetur adipiscing elit, \nsed do eiusmod \ntempor incididunt ut \nlabore et dolore \nmagna aliqua.", font = "Verdana 9", width = 22, justify=LEFT, bg="#9CE0ED" , wrap=250,  borderwidth=1 , relief=SOLID)
        self.endscreen_text.grid(row=1)

        #Dismiss button 2 
        self.tryagain_button = Button(self.endscreen_frame, text="Exit", width=10,font="garamond 12",)
        self.tryagain_button.grid(row=2,pady=10)
    



class Quiz_10:
    def __init__(self, mode, partner):
        print(mode)
        self.test =IntVar()
        self.test.set(mode)
        #set up list to hold questions
        questions = []
        #opens a new window
        self.quiz_10_box = Toplevel()
        #makes the X button in the corner functional
        self.quiz_10_box.protocol('WM_DELETE_WINDOW', partial(self.close_button, partner))
        #frame to hold components
        self.answer_frame = Frame(self.quiz_10_box, width=400, height= 200, bg = "#B1DDF0")
        self.answer_frame.grid(row=0, column = 0)
        self.counter = Label(self.answer_frame, text="{}/10", font = "garamond 14", bg ="#B1DDF0" )
        self.counter.grid(row = 0, sticky=NW)
        self.question = Label(self.answer_frame, text= "?",  font = "garamond 14", bg ="#B1DDF0" )
        self.question.grid(row=1, column = 0)
        self.a1=Button(self.answer_frame,text = "", width = 10, height = 1 ,font="garamond 14" , background="#FFFF88")
        self.a1.grid(row = 2, column = 0, padx=10, pady=10)
        self.a2 = Button(self.answer_frame,text = "", width = 10, height = 1 ,font="garamond 14" , background="#CCE5FF")
        self.a2.grid(row = 3, column = 0, padx=10, pady=10)
        self.a3 = Button(self.answer_frame,text = "", width = 10, height = 1 ,font="garamond 14" , background="#CDEB8B")
        self.a3.grid(row = 2, column = 1,  padx=10, pady=10)
        self.a4=Button(self.answer_frame,text = "", width = 10, height = 1 ,font="garamond 14" , background="#FFFF88")
        self.a4.grid(row = 3, column = 1,  padx=10, pady=10) 
        self.click_btn= PhotoImage(file='Music_Quiz\play_fixed_small.gif')
        self.img_2= PhotoImage(file='Music_Quiz\pause_fixed_small.gif')
        self.play_button= Button(self.answer_frame, borderwidth=0, background = "#B1DDF0")
        self.play_button.config(image = self.click_btn)
        self.play_button.grid(row=1,column=1)


    def play(self, partner):
        self.play_button.config(image = self.img_2)

    def close_button(self, partner):
        #destory the currently open box
        self.quiz_10_box.destroy()
        #bring back the root box
        root.deiconify()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    something = Start(root)
    root.mainloop()