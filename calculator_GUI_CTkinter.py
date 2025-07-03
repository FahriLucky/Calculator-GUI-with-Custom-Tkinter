from customtkinter import *
from tkinter import*

#structure ui
app = CTk()
app.geometry('500x800')
app.resizable(False, False) 
app.title('Calculator by CTkinter(python)')
set_appearance_mode('dark')

#title
title = CTkLabel(master= app, text='Calculator by python')
title.place(relx = 0.5 , rely = 0.08, anchor ='center')
title.configure(font=('Futura', 25,'bold'))
                
            
#input/display
input_numbers = StringVar() #--->display to entry
operator = '' #--> collect data into a string

display = CTkEntry(master=app,placeholder_text='Masukan numbers', textvariable=input_numbers)
display.place(relx = 0.5 , rely = 0.2, anchor ='center')
display.configure(width= 400,
                  height = 60,
                  fg_color = '#262729',
                  border_color = 'white',
                  corner_radius = 20
                  ) 


#main operation calculator
def btn_click(num): #collect the input data
    global operator
    operator = operator + str(num)
    input_numbers.set(operator) # --> show numbers on the screen

def answer(): #Operation math
    global operator
    answ = str(eval(operator))
    input_numbers.set(answ) # # --> show numbers on the screen
    # operator= ''

def clear():  #--> clear the data
    global operator
    operator =  ''
    input_numbers.set('') 



#button numbers and operation
def operation_button(oper:str,x:int,y:int, commen:str):
    button_operasi =CTkButton(master=app,text=oper,command=lambda:btn_click(commen))
    button_operasi.place(relx = x , rely = y, anchor ='center')
    button_operasi.configure(width  = 98,
                             height = 90,
                             fg_color = '#1a8742',
                             hover_color = "#144c29")
    
def answer_and_clear(oper:str,x:int,y:int,iscommen): 
    button_operasi =CTkButton(master=app,text=oper, command=lambda:iscommen()) 
    button_operasi.place(relx = x , rely = y, anchor ='center') 
    button_operasi.configure(width  = 98, height = 90, fg_color = '#1a8742', hover_color = "#144c29")

#layout button
#(1 2 3 4 5) ---> line(x)
#(2) |
#(3) |
#(4) v
#(5) column (y)
column1= 0.4
column2 = 0.52
column3 = 0.64
column4 = 0.76
column5 = 0.88

line1 = 0.19
line2 = 0.4
line3 = 0.612
line4 = 0.82


# clear k2 , b1
            #(name btn, x,    y,    comment)
answer_and_clear('C',line1,column1, clear)

# . k3 , b1
operation_button('.',line2,column1, '.')

# % k4 , b1
operation_button('%',line3 ,column1, '%')

# x k5 , b1
operation_button('x',line4, column1 , '*')

# ÷
operation_button('÷',line4, column2 , '/')

# +
operation_button('+',line4, column3, '+' )

# -
operation_button('-',line4, column4, '-' )

# =
answer_and_clear('=',line4, column5, answer)

#number buttons
def numbers_button(oper:str,x:int,y:int,comen:str):
    button_numbers =CTkButton(master=app,text=oper, command=lambda:btn_click(comen))
    button_numbers.place(relx = x , rely = y, anchor ='center')
    button_numbers.configure(width  = 98,
                             height = 90,
                             fg_color = "#555757",
                             hover_color = "#353636"
                             )

#7
numbers_button('7',line1, column2, 7)

#8
numbers_button('8',line2, column2, 8)

#9
numbers_button('9',line3, column2, 9)

#4
numbers_button('4',line1, column3, 4)

#5
numbers_button('5',line2, column3, 5)

#6
numbers_button('6',line3, column3 ,6)

#1
numbers_button('1',line1, column4, 1)

#2
numbers_button('2',line2, column4, 2)

#3
numbers_button('3',line3, column4, 3)

#(
operation_button('(',line1, column5, '(' )

#0
numbers_button('0',line2, column5, 0)

#)
operation_button(')',line3, column5, ')')

app.mainloop()