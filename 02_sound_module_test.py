from tkinter import *
from winsound import *
class Start:
    def __init__(self, parent):

        # Bkg Variable
        bkg_colour = "#9fe5d9"

        # Main Window
        self.start_frame = Frame(width=400, height=300, bg=bkg_colour, padx=10, pady=30)
        
        self.start_frame.grid()
  
        #Help button
        self.noise_button_01 = Button(self.start_frame, text="Success", padx=10, pady=10, command = self.play)
        self.noise_button_01.grid(row=1)
        
        self.noise_button_02 = Button(self.start_frame, text="Beep", padx=10, pady=10, command = self.play2 )
        self.noise_button_02.grid(row=2)
        
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
