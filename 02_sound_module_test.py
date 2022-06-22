from tkinter import *
from winsound import *
class Start:
    def __init__(self, parent):

         # Bkg Variable
        start_bkg = "#BAC8D3"

        # Main Window
        self.start_frame = Frame(width=240, height=150, bg=start_bkg, padx=10, pady=15)
        
        self.start_frame.grid()
  
        #Help button
        self.noise_button_01 = Button(self.start_frame, text="Play Sound",  command = self.play)
        self.noise_button_01.grid(row=1,padx=20, pady=20)
        
        self.noise_button_02 = Button(self.start_frame, text="Beep", command = self.play2)
        self.noise_button_02.grid(row=2, padx=20, pady=20)
        
        #title
        self.start_label = Label(self.start_frame, text = "Sound Player", font="garamond 20 bold", justify=LEFT, bg=start_bkg)
        self.start_label.grid(row=0, sticky=NW)

    def play2(self):
        return Beep(800,500)
    def play(self):
        return PlaySound("03_20th_Century_Music_Quiz\success-1-6297.wav", SND_FILENAME | SND_ASYNC)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Sound Player")
    something = Start(root)
    root.mainloop()
