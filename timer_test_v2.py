import tkinter as tk
class Timer():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="", font=('Times New Roman', 40))
        self.label.pack()
        self.updateClock()
        self.root.mainloop()
    def updateClock(self,count):
        # change text in label        
        self.label['text'] = count

        if count > 0:
       
            self.root.after(1000, self.updateClock, count-1)

        root = tk.Tk()

        label = tk.Label(root)
        label.place(x=35, y=15)

    updateClock(60)

