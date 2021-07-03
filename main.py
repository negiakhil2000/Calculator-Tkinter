from tkinter import*
calc = Tk()
calc.title('Calculator')
calc.geometry('350x450')
calc.configure(bg='#ffccff')
calc.resizable(width=False,height=False) #you can also use just (False,Fasle)
calc.iconbitmap('icon.ico')
expression = ''
def press(num):
    global expression
    expression = expression + str(num)
    eq.set(expression)
def equalpress():
    global expression
    try:
        total = str(eval(expression))
        eq.set(total)
        expression = total
        expression = ''
    except:
        eq.set('error')
        expression = ''


def clear():
    global expression
    eq.set('0')
    expression=''





button_frame=Frame(calc,bg='#ffccff')
button_frame.pack()
eq=StringVar()
entry_field=Entry(button_frame,textvariable=eq,
                  justify='right',font=('arial',20,'bold'))
entry_field.pack(pady=10)
#button-row1
button_row1=Frame(calc,bg='#ffccff')
button_row1.pack(expand=True,fill='both')

button1=Button(button_row1,text='1',font=('cambria',12),
               relief='groove',borderwidth='1',bg='#ff80ff',width=9,height=4,
               command=lambda:press(1))
button1.pack(side=LEFT,expand=True,fill='both')

button2=Button(button_row1,text='2',font=('cambria',12),
               relief='groove',borderwidth='1',bg='#ff80ff',width=9,height=4,
               command=lambda:press(2))
button2.pack(side=LEFT,expand=True,fill='both')

button3=Button(button_row1,text='3',font=('cambria',12),
               relief='groove',borderwidth='1',bg='#ff80ff',width=9,height=4,
               command=lambda:press(3))
button3.pack(side=LEFT,expand=True,fill='both')

button_plus=Button(button_row1,text='+',font=('cambria',12),
               relief='groove',borderwidth='1',bg='#ff80ff',width=9,height=4,
               command=lambda:press('+'))
button_plus.pack(side=LEFT,expand=True,fill='both')

#button row2

button_row2=Frame(calc,bg='#ffccff')
button_row2.pack(expand=True,fill='both')

button4=Button(button_row2,text='4',font=('cambria',12),
               relief='groove',borderwidth='1',bg='#ff80ff',width=9,height=4,
               command=lambda:press(4))
button4.pack(side=LEFT,expand=True,fill='both')

button5=Button(button_row2,text='5',font=('cambria',12),
               relief='groove',borderwidth='1',bg='#ff80ff',width=9,height=4,
               command=lambda:press(5))
button5.pack(side=LEFT,expand=True,fill='both')

button6=Button(button_row2,text='6',font=('cambria',12),
               relief='groove',borderwidth='1',bg='#ff80ff',width=9,height=4,
               command=lambda:press(6))
button6.pack(side=LEFT,expand=True,fill='both')

button_minus=Button(button_row2,text='-',font=('cambria',12),
               relief='groove',borderwidth='1',bg='#ff80ff',width=9,height=4,
               command=lambda:press('-'))
button_minus.pack(side=LEFT,expand=True,fill='both')

#button-row3

button_row3=Frame(calc,bg='#ffccff')
button_row3.pack(expand=True,fill='both')

button7=Button(button_row3,text='7',font=('cambria',12),
               relief='groove',borderwidth='1',bg='#ff80ff',width=9,height=4,
               command=lambda:press(7))
button7.pack(side=LEFT,expand=True,fill='both')

button8=Button(button_row3,text='8',font=('cambria',12),
               relief='groove',borderwidth='1',bg='#ff80ff',width=9,height=4,
               command=lambda:press(8))
button8.pack(side=LEFT,expand=True,fill='both')

button9=Button(button_row3,text='9',font=('cambria',12),
               relief='groove',borderwidth='1',bg='#ff80ff',width=9,height=4,
               command=lambda:press(9))
button9.pack(side=LEFT,expand=True,fill='both')

button_mul=Button(button_row3,text='*',font=('cambria',12),
               relief='groove',borderwidth='1',bg='#ff80ff',width=9,height=4,
               command=lambda:press('*'))
button_mul.pack(side=LEFT,expand=True,fill='both')

#button-row4
button_row4=Frame(calc,bg='#ffccff')
button_row4.pack(expand=True,fill='both')

button_dec=Button(button_row4,text='.',font=('cambria',12),
               relief='groove',borderwidth='1',bg='#ff80ff',width=9,height=4,
               command=lambda:press('.'))
button_dec.pack(side=LEFT,expand=True,fill='both')
button0=Button(button_row4,text='0',font=('cambria',12),
               relief='groove',borderwidth='1',bg='#ff80ff',width=9,height=4,
               command=lambda:press(0))
button0.pack(side=LEFT,expand=True,fill='both')
button_c=Button(button_row4,text='C',font=('cambria',12),
               relief='groove',borderwidth='1',bg='#ff80ff',width=9,height=4,
               command=clear)
button_c.pack(side=LEFT,expand=True,fill='both')
button_div=Button(button_row4,text='/',font=('cambria',12),
               relief='groove',borderwidth='1',bg='#ff80ff',width=9,height=4,
               command=lambda:press('/'))
button_div.pack(side=LEFT,expand=True,fill='both')


#button-row5

button_row5 = Frame(calc,bg='#ffccff')
button_row5.pack(expand=True,fill='both')

button_equals=Button(button_row5,text=' = ',font=('cambria',12),
               relief='groove',borderwidth='1',bg='#ff80ff',width=9,height=4,
               command=lambda:equalpress())
button_equals.pack(side=LEFT,expand=True,fill='both')
calc.mainloop()





