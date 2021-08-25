from words_list import words
from tkinter import *
import random
import sys
import os

# number of seconds of the countdown
countdown_seconds = 60
# set countdown text value to be replaced later (and deleted before the new number gets displayed) => check countdown()
countdown_text = 0
# to launch the countdown only when ppl start typing
once = 0
# first word of the displayed list
words_first = 0
# indice value for word validation
indice = 0
# list of typed word
indice_list = []

# generation of a list of 200 english random words
test_list = []
for number in range(0,200):
    test_list.append(words[random.randint(0,999)])

# to restart the and try the test again
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# to launch the countdown and then calculate the score (CPM and WPM at the end)
def countdown():
    global countdown_seconds, countdown_text
    canvas.delete(countdown_text)
    countdown_seconds -= 1
    countdown_text = canvas.create_text(400, 190,font="DINAlternate 50 bold", text=countdown_seconds, fill="#00adb5")
    if countdown_seconds == 0:
        str_indice_list = " ".join([str(word) for word in indice_list])
        cpm = len(str_indice_list)
        wpm = round(cpm/5)
        score = canvas.create_text((400, 495), text=f"Your score: {cpm} CPM (that is {wpm} WPM)", font="DINAlternate 30",
                                           fill="#00adb5")
    else:
        canvas.after(1000, countdown)

# to check what user enters in the field, compare it with the list words and delete it from the list of words to type
def start_count():
    global once, words_first, indice, indice_list
    input = text_field.get("1.0",'end-1c')
    if once == 0:
        if input != "":
            countdown()
            once += 1
    if " " in input:
        text_field.delete("1.0", 'end-1c')
        if input.split(" ")[0] == test_list[indice]:
            indice_list.append(test_list[indice])
            indice += 1
        else:
            indice += 1
        words_first += 1
        words_last = words_first + 20
        canvas.itemconfig(words_to_type,text=test_list[words_first:words_last])
    canvas.after(1, start_count)

# Create the window
window = Tk()
window.title("Typing Speed Test by JJ")
window.config(width=800,height=600,padx=50, pady=50,bg="#393e46")
canvas = Canvas(window,width=800, height=600, bg="#aad8d3")
canvas.grid(column=0,row=0)

#Add the text, list of words, text field and restart button
label_msg = canvas.create_text((400, 90), text="Test your Typing Speed !", font="DINAlternate 50 bold", fill="#393e46")
words_to_type = canvas.create_text((400,320),justify="left",text = test_list[:20], width = 550,font="DINAlternate 30", fill="#393e46")
text_field = Text(canvas, height=1, width=30,font="DINAlternate 30")
text_field.place(x=130,y=420)
restart = Button(canvas, padx=10, pady=10, text="Restart",highlightbackground='#393e46', font="DINAlternate", command=restart_program)
restart.place(x=350, y=520)

window.after(1,start_count)

window.mainloop()