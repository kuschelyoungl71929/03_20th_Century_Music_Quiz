from tkinter import * 
class Timer:
    def __init__(self):
        self.frame = Frame(width = 200, height = 200)
        self.frame.grid()
        self.countdown(60)
    def countdown(self, count):
        self.label = Label(self.frame, text = count,font=('Times New Roman', 40))
        self.label.grid(row = 1, column = 1)
        
        if count > 0:
        
            root.after(1000, self.countdown, count-1)

if __name__ == "__main__":
    root = Tk()
    root.title("Timer")
    something = Timer()
    root.mainloop()