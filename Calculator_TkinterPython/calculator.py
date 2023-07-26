# Calculator in Python
from tkinter import *

cal = Tk()
cal.title("Simple Calculator")
cal.geometry('360x400')

def click(number):
    global operator
    operator = operator + str(number)
    variable.set(operator)

def clear():
    global operator
    operator = ""
    variable.set(operator)

def sum():
    global operator
    operator = str(eval(operator))
    variable.set(operator)
operator=""

variable = StringVar()
display = Entry(cal,font=('arial',20,'bold'),bd=25,textvariable=variable,justify='right')
display.grid(columnspan=5)

button1 = Button(cal,text='1',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click(1))
button1.grid(row=3,column=0)

button2 = Button(cal,text='2',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click(2))
button2.grid(row=3,column=1)

button3 = Button(cal,text='3',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click(3))
button3.grid(row=3,column=2)

button0 = Button(cal,text='0',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click(0))
button0.grid(row=4,column=0)

buttonpoint = Button(cal,text=' .',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click('.'))
buttonpoint.grid(row=4,column=1)


buttonclear = Button(cal,text='C',font=('arial',20,'bold'),bd=5,padx=10,command = clear)
buttonclear.grid(row=4,column=2)

buttonplus = Button(cal,text='+',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click('+'))
buttonplus.grid(row=1,column=4)

buttonminus = Button(cal,text='-',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click('-'))
buttonminus.grid(row=2,column=4)

buttonmulti = Button(cal,text='*',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click('*'))
buttonmulti.grid(row=3,column=4)

buttondiv = Button(cal,text='/',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click('/'))
buttondiv.grid(row=4,column=4)

buttonequal = Button(cal,text='=',font=('arial',20,'bold'),bd=5,padx=140,command = sum)
buttonequal.grid(row=5,columnspan=5)



button7 = Button(cal,text='7',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click('7'))
button7.grid(row=1,column=0)

button8 = Button(cal,text='8',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click('8'))
button8.grid(row=1,column=1)

button9 = Button(cal,text='9',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click('9'))
button9.grid(row=1,column=2)

button4 = Button(cal,text='4',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click('4'))
button4.grid(row=2,column=0)

button5 = Button(cal,text='5',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click('5'))
button5.grid(row=2,column=1)

button6 = Button(cal,text='6',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click('6'))
button6.grid(row=2,column=2)

cal.mainloop()
