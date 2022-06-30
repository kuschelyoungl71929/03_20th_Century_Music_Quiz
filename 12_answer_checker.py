from tkinter import *
from functools import partial #for removing window
import random


class Quiz_timed:
    def __init__(self partner):
        #opens a new window
        self.quiz_10_box = Toplevel()
        #makes the X button in the corner functional
        self.quiz_10_box.protocol('WM_DELETE_WINDOW', partial(self.close_button, partner))
        #frame to hold components
        self.answer_frame = Frame(self.quiz_10_box, width=400, height= 200, bg = "#B1DDF0")
        self.answer_frame.grid(row=0, column = 0)
        self.counter = Label(self.answer_frame, text="", font = "garamond 14", bg ="#B1DDF0" )
        self.counter.grid(row = 0, sticky=NW)
        self.countdown(60)
        self.question = Label(self.answer_frame, text= "?",  font = "garamond 14", bg ="#B1DDF0" )
        self.question.grid(row=1, column = 0)
        self.a1=Button(self.answer_frame,text = "", width = 10, height = 1 ,font="garamond 14" , background="#CDEB8B", command= lambda: [self.question_rng(partner)])
        self.a1.grid(row = 2, column = 0, padx=10, pady=10)
        self.a2 = Button(self.answer_frame,text = "", width = 10, height = 1 ,font="garamond 14" ,background="#CDEB8B", command= lambda: [self.question_rng(partner)])
        self.a2.grid(row = 3, column = 0, padx=10, pady=10)
        self.a3 = Button(self.answer_frame,text = "", width = 10, height = 1 ,font="garamond 14" , background="#CDEB8B", command= lambda: [self.question_rng(partner)])
        self.a3.grid(row = 2, column = 1,  padx=10, pady=10)
        self.a4=Button(self.answer_frame,text = "", width = 10, height = 1 ,font="garamond 14" , background="#CDEB8B", command= lambda: [self.question_rng(partner)])
        self.a4.grid(row = 3, column = 1,  padx=10, pady=10) 
        self.question_rng(partner)

    

    def question_rng(self, partner):
        #set up list to hold questions
        questions = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]
        self.a1.configure(text = "",command= lambda: [self.question_rng(partner)])
        self.a2.configure(text = "",command= lambda: [self.question_rng(partner)])
        self.a3.configure(text = "",command= lambda: [self.question_rng(partner)])
        self.a4.configure(text = "",command= lambda: [self.question_rng(partner)])
        for item in range(0, 1): 

            for thing in range(0,1):

                q_num = random.randint(1,15)
                questions += ""
            
                if q_num == 1:
                    file = questions[0]
                    self.a1.configure(text ="b", command= lambda: [self.question_rng(partner), self.answerchecker()])
                elif q_num == 2:
                    file = questions[1]
                    self.a2.configure(text ="c",command= lambda: [self.question_rng(partner), self.answerchecker()])
                elif  q_num == 3:
                    file = questions[2]
                    self.a3.configure(text ="d",command= lambda: [self.question_rng(partner), self.answerchecker()])
                elif q_num == 4:
                    file = questions[3]
                    self.a4.configure(text ="e",command= lambda: [self.question_rng(partner), self.answerchecker()])
                elif q_num == 5:
                    file = questions[4]
                    self.a1.configure(text ="f",command= lambda: [self.question_rng(partner), self.answerchecker()])
                elif q_num == 6:
                    file = questions[5]
                    self.a2.configure(text ="g",command= lambda: [self.question_rng(partner), self.answerchecker()])
                elif q_num == 7:
                    file = questions[6]
                    self.a3.configure(text ="h",command= lambda: [self.question_rng(partner), self.answerchecker()])
                elif  q_num == 8:
                    file = questions[7]
                    self.a4.configure(text ="i",command= lambda: [self.question_rng(partner), self.answerchecker()])
                elif q_num == 9:
                    file = questions[8]
                    self.a1.configure(text ="j",command= lambda: [self.question_rng(partner), self.answerchecker()])
                elif q_num == 10:
                    file = questions[9]
                    self.a2.configure(text ="k",command= lambda: [self.question_rng(partner), self.answerchecker()])
                elif q_num == 11:
                    file = questions[10]
                    self.a3.configure(text ="l",command= lambda: [self.question_rng(partner), self.answerchecker()])
                elif q_num == 12:
                    file = questions[11]
                    self.a4.configure(text ="m",command= lambda: [self.question_rng(partner), self.answerchecker()])
                elif  q_num == 13:
                    file = questions[12]
                    self.a1.configure(text ="n",command= lambda: [self.question_rng(partner), self.answerchecker()])
                elif q_num == 14:
                    file = questions[13]
                    self.a2.configure(text ="o",command= lambda: [self.question_rng(partner), self.answerchecker()])
                elif q_num == 15:
                    file = questions[14]
                    self.a3.configure(text ="p",command= lambda: [self.question_rng(partner), self.answerchecker()])

                        
        
        #display images
        self.question.configure(text=file)

    def countdown(self, count):
        self.counter.configure(text = count)
        self.counter.grid(row = 1, column = 1)
        
        if count > 0:
        
            root.after(1000, self.countdown, count-1)
        else: 
            self.close_button(self)

    def close_button(self, partner):
        #destory the currently open box
        self.quiz_10_box.destroy()
        #bring back the root box
        root.deiconify()
    def answerchecker(self):
        print("correct")

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Quiz_timed(root)
    root.mainloop()
