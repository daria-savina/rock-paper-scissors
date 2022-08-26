import random
from tkinter import *

root = Tk()

root['bg'] = '#fafafa'
root.title('Game')
root.geometry('510x380')
root.resizable(width=False, height=False)

canvas = Canvas(root, height=510, width=400)
canvas.grid()

frame = Frame(root, bg="#F5FFFA")
frame.place(relwidth=1, relheight=1)

# -------------------------------------------
x = ['rock', 'paper', 'scissors']

comp_choise = ''
your_choise = ''

comp_win = 0
your_win = 0


def click_button(text):
    global your_choise
    your_choise = text
    your_ch.config(text="Player: {}".format(your_choise))

    ran()

    calculateResult()


def calculateResult():
    res = ''
    global your_win
    global comp_win

    if (your_choise == 'rock') and (comp_choise == 'scissors'):
        res = 'You win. Rock bits Scissors!'
        your_win += 1
    elif (your_choise == 'rock') and (comp_choise == 'paper'):
        comp_win += 1
        res = 'You lose. Paper bits Rock!'
    elif (your_choise == 'rock') and (comp_choise == 'rock'):
        res = 'Dead heat.'

    elif (your_choise == 'paper') and (comp_choise == 'rock'):
        res = 'You win. Paper bits Rock!'
        your_win += 1
    elif (your_choise == 'paper') and (comp_choise == 'scissors'):
        res = 'You lose. Scissors bits Paper!'
        comp_win += 1
    elif (your_choise == 'paper') and (comp_choise == 'paper'):
        res = 'Dead heat.'

    elif (your_choise == 'scissors') and (comp_choise == 'paper'):
        res = 'You win. Scissors bits Paper!'
        your_win += 1
    elif (your_choise == 'scissors') and (comp_choise == 'rock'):
        res = 'You lose. Rock bits Scissors!'
        comp_win += 1
    elif (your_choise == 'scissors') and (comp_choise == 'scissors'):
        res = 'Dead heat.'

    result['text'] = '{}'.format(res)
    stat['text'] = "You {} : Comp {}".format(your_win, comp_win)


def ran():
    global comp_choise
    comp_choise = random.choice(x)
    result.configure(fg='red')
    comp_ch['text'] = 'Computer: {}'.format(comp_choise)


def deleteTask():
    result.config(text="Click to start again!", bg="#F5FFFA", fg="#800080")

    global your_win
    your_win = 0
    global comp_win
    comp_win = 0

    stat['text'] = "You {} : Comp {}".format(your_win, comp_win)

# ------------------------------------------------

button_1 = Button(frame, text="paper",
                  width=20,
                  height=5,
                  bg="#5F9EA0",
                  fg="#E0FFFF",
                  font="Arial 9",
                  command=lambda: click_button('paper')).grid(row=2, column=2, padx=5, pady=5)

button_2 = Button(frame, text="scissors",
                  width=20,
                  height=5,
                  bg="#5F9EA0",
                  fg="#E0FFFF",
                  font="Arial 9",
                  command=lambda: click_button('scissors')).grid(row=2, column=3, padx=5, pady=5)

button_3 = Button(frame, text="rock",
                  width=20,
                  height=5,
                  bg="#5F9EA0",
                  fg="#E0FFFF",
                  font="Arial 9",
                  command=lambda: click_button('rock')).grid(row=2, column=4, padx=5, pady=5)

delTask_btn = Button(
    frame,
    text='Reset',
    bg='#696969',
    font="Arial 10",
    command=deleteTask)
delTask_btn.grid(row=9, column=1, columnspan=5, padx=5, pady=5)
# ----------------------------
result = Label(frame, text="Click above to start!",
               bg="#F5FFFA",
               fg="#4682B4",
               borderwidth=10,
               width=40,
               font="Arial 15")
result.grid(row=4, column=1, columnspan=5, padx=5, pady=5)

your_ch = Label(frame, text="Player: ", bg="#F5FFFA", fg="#808080", width=20, height=2, font="Arial 12")
your_ch.grid(row=5, column=1, columnspan=5, padx=5, pady=5)

comp_ch = Label(frame, text="Computer: ", bg="#F5FFFA", fg="#808080", width=20, height=2, font="Arial 12")
comp_ch.grid(row=6, column=1, columnspan=5, padx=5, pady=5)

stat = Label(frame, text="You 0 : Comp 0",
             bg="#F5FFFA",
             fg="#4682B4",
             borderwidth=10,
             width=40,
             font="Arial 15")
stat.grid(row=7, column=1, columnspan=5, padx=5, pady=5)

root.mainloop()
