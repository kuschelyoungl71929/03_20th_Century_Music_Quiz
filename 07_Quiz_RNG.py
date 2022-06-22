
from tkinter import * 
from functools import partial
import random

NUM_TRIALS = 1
questions = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]

for item in range(0, NUM_TRIALS): 
    question = 0
    qnum = 0
   
    for thing in range(0,1):

        prize_num = random.randint(1,15)
        questions += " "
        
        if prize_num == 1:
            file = questions[1]
        
        elif prize_num == 2:
            file = questions[2]

        elif  prize_num == 3:
          file = questions[3]

        elif prize_num == 4:
            file = questions[4]

        elif prize_num == 5:
            file = questions[5]

        elif prize_num == 6:
            file = questions[6]

        elif prize_num == 7:
            file = questions[7]

        elif  prize_num == 8:
          file = questions[8]

        elif prize_num == 9:
            file = questions[9]

        elif prize_num == 10:
            file = questions[10]

        elif prize_num == 11:
            file = questions[11]

        elif prize_num == 12:
            file = questions[12]

        elif  prize_num == 13:
          file = questions[13]
   
        elif prize_num == 14:
            file = questions[14]

        elif prize_num == 15:
            file = questions[15]
           

    print(file)
