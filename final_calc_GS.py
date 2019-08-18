from tkinter import  *
from math import *

my_window=Tk()
my_window.title("Calculator ----Gurendar")

width_window=465
height_window=550
screen_width=my_window.winfo_screenwidth()
screen_height=my_window.winfo_screenheight()

x_cod=(screen_width/2-width_window/2)
y_cod=(screen_height/2-height_window/2)

my_window.geometry("%dx%d+%d+%d"%(width_window,height_window,x_cod,y_cod))

str_value = StringVar()
str_value.set("")
test = ""
def on_click(event):
    # text = event.widget.cget("text")
    global text, txt_window, test
    text = (event)
    str_value.set(str_value.get() + str(text))
    test = str_value.get()
    txt_window.update()

def Clear():
    global  text, str_value
    str_value.set("")
    txt_window.update()

def add_op():
    global  n1,temp,operation,test
    n1 = float(test)
    operation = 'add'
    str_value.set("")
    txt_window.update()
def sub_op():
    global  n1,temp,operation,test
    print("I am in sub function")
    n1 = float(test)
    operation = 'sub'
    str_value.set("")
    txt_window.update()

def multi_op():
    global  n1,temp,operation,test
    n1 = float(test)
    operation = 'multi'
    str_value.set("")
    txt_window.update()

def div_op():
    global  n1,temp,operation,test
    n1 = float(test)
    operation = 'div'
    str_value.set("")
    txt_window.update()

def Sqroot_op():
    global  n1,sq_root_result
    n1 = float(test)
    sq_root_result = sqrt(n1)
    str_value.set(sq_root_result)
    txt_window.update()

def Inverse_op():
    global  n1,inverse_result
    n1 = float(test)
    # if n1 == 0:
    #     str_value.set("Invalid: Please press cancel")
    #     # my_window.destroy()
    # else:
    inverse_result = (1/n1)
    str_value.set(inverse_result)
    txt_window.update()

def sq_op():
    global  n1,sq_result
    print("I am in Inverse function")
    n1 = float(test)
    sq_result = (n1*n1)
    str_value.set(sq_result)
    txt_window.update()

def show_result():
    global n2, total,operation
    n2 =float(test)
    print(operation)
    str_value.set("")
    txt_window.update()

    if operation == 'add':
        total = n1+n2
        str_value.set(total)
        txt_window.update()
    elif operation == 'sub':
        total = n1 - n2
        str_value.set(total)
        txt_window.update()
    elif operation == 'multi':
        total = n1 * n2
        str_value.set(total)
        txt_window.update()

    elif operation == 'div':
        total = n1/n2
        str_value.set(total)
        txt_window.update()
    else:
        pass

txt_window = Entry(my_window,textvariable = str_value, font =('arial', 20, 'bold'),
                   bg = 'powder blue', bd = 20, width = 28,justify = 'right')
txt_window.grid(row =0,column = 0, columnspan = 4, pady = 1)
txt_window.insert(0,'')

frame_button = Frame(my_window, bg = 'powder blue')
frame_button.grid()

numberpad =[7,8,9,4,5,6,1,2,3,0]
i = 0
btn = []
btn_txt = []

for j in range(2,5):
    for col in range(3):
        btn.append(Button(frame_button, width = 6, height = 2,
                          font = 'arial 20 bold', bg = 'powder blue', bd = 4,
                                text = numberpad[i]))
        btn[i].grid(row = j, column = col, pady = 1)
        p = btn[i].cget('text')
        btn_txt.append(p)
        btn[i]['command'] = lambda x=numberpad[i]: on_click(x)
        i += 1

btnC = (Button(frame_button, width = 6, height = 2, font = 'arial 20 bold',
                bg = 'powder blue', bd = 4,text = 'C',
                    command = Clear))
btnC.grid(row = 1, column = 0, pady = 1)

btnSquare_root = (Button(frame_button, width = 6, height = 2, font = 'arial 20 bold',
            bg = 'powder blue', bd = 4,text = '√',
                command = Sqroot_op))
btnSquare_root.grid(row = 1,column = 1, pady = 1)

btnInverse = (Button(frame_button, width = 6, height = 2, font = 'arial 20 bold',
            bg = 'powder blue', bd = 4,text = '1/x',
                command = Inverse_op))
btnInverse.grid(row = 1,column = 2, pady = 1)

btnsq = (Button(frame_button, width = 6, height = 2, font = 'arial 20 bold',
            bg = 'powder blue', bd = 4,text = 'x^2',
                command = sq_op))
btnsq.grid(row = 1,column = 3, pady = 1)

btnAdd = (Button(frame_button, width = 6, height = 2, font = 'arial 20 bold',
            bg = 'powder blue', bd = 4,text = '+', command = add_op))
btnAdd.grid(row = 2, column = 3,pady = 1)

btnEquals = (Button(frame_button, width = 6, height = 2, font = 'arial 20 bold',
            bg = 'powder blue', bd = 4,text = '=',
                command = show_result))
btnEquals.grid(row = 5, column = 2, pady = 1)

btn0 = (Button(frame_button, width = 6, height = 2, font = 'arial 20 bold',
            bg = 'powder blue', bd = 4,text = '0',
                command = lambda x=0: on_click(x)))
btn0.grid(row = 5,column = 0, pady = 1)

btnDot = (Button(frame_button, width = 6, height = 2, font = 'arial 20 bold',
            bg = 'powder blue', bd = 4,text = '.',
                command = lambda x='.': on_click(x)))
btnDot.grid(row = 5,column = 1, pady = 1)

btnSub = (Button(frame_button, width = 6, height = 2, font = 'arial 20 bold',
            bg = 'powder blue', bd = 4,text = '-',
                command = sub_op))
btnSub.grid(row = 3,column = 3, pady = 1)

btnMulti = (Button(frame_button, width = 6, height = 2, font = 'arial 20 bold',
            bg = 'powder blue', bd = 4,text = '*',
                command = multi_op))
btnMulti.grid(row = 4,column = 3, pady = 1)

btnDiv = (Button(frame_button, width = 6, height = 2, font = 'arial 20 bold',
            bg = 'powder blue', bd = 4,text = '/',
                command = div_op))
btnDiv.grid(row = 5,column = 3, pady = 1)

my_window.mainloop()