# Tic-Tac-Toe.....Corrected
# Second Approach)

from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe - Gurendar")
tk.resizable(width=0, height=0)

global button1,button2,button3,button4,button5,button6,button7,button8,button9
buttons = StringVar()
first_player = StringVar()
second_player = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

bclick = True
flag = 1
msg_1=""
msg_2=""


def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

def enableButton():
    flag=1
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    button1.configure(state=ACTIVE)
    button2.configure(state=ACTIVE)
    button3.configure(state=ACTIVE)
    button4.configure(state=ACTIVE)
    button5.configure(state=ACTIVE)
    button6.configure(state=ACTIVE)
    button7.configure(state=ACTIVE)
    button8.configure(state=ACTIVE)
    button9.configure(state=ACTIVE)
    # buttons["text"]=""


def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, second_player, first_player
    second_player = p2.get() + " Won!"
    first_player = p1.get() + " Won!"
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        checkForWin()
        flag += 1
    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    global flag
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    global msg_1
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        msg_1=tkinter.messagebox.showinfo("Tic-Tac-Toe", first_player)
        tk.quit()
        # end_popup()
        # print(msg_1)

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
          disableButton()
          tkinter.messagebox.showinfo("Tic-Tac-Toe", second_player)
          tk.quit()

    elif flag ==9:
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Match is a Tie")
        tk.quit()

    else:
        pass
# def end_popup():
#     global tk
#     if msg_1 == "ok":
#         global msg_2
#         # msg2=tkinter.messagebox.showinfo("Tic-Tac-Toe", Do you)
#         msg_2 = tkinter.messagebox.askyesno("Tic Tac Toe ",message="Do you want to continue?")
#         print(msg_2)
#     elif msg_2 == False:
#         tk.quit()
#     elif msg_2==True:
#         tk.update()
        # game_restart()

    # else:
    #     pass
# def game_restart():
#     global button1, button2, button3, button4, button5, button6, button7, button8, button9
#     enableButton()
#     button1['text']=''
#     button2["text"]=""

label = Label( tk, text="Player 1:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=1, column=0)

label = Label( tk, text="Player 2:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=0)

button1 = Button(tk, text=" ", font='Times 20 bold', bg='Lime', fg='blue', height=4, width=8,
          command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='Lime', fg='blue', height=4, width=8,
          command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='Lime', fg='blue', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='Lime', fg='blue', height=4, width=8,
          command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='Lime', fg='blue', height=4, width=8,
          command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='Lime', fg='blue', height=4, width=8,
          command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='Lime', fg='blue', height=4, width=8,
          command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='Lime', fg='blue', height=4, width=8,
          command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='Lime', fg='blue', height=4, width=8,
           command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

# game_restart()
tk.mainloop()
