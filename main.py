from tkinter import *
window=Tk()
window.geometry("450x550")
window.title("GUI Calcy")
window.configure(bg="#70214f")
window.iconbitmap("calculator_icon.ico")

expression=""
def press(n):
	global expression
	if n=='x':
		expression+="*"
	else:
	    expression+=str(n)
	equation.set(expression)
def result():
	try:
		global expression
		total=str(eval(expression))
		equation.set(total);expression=""
	except:
		equation.set('Error!!!')
		expression=""

def clear():
	global expression
	expression=""
	equation.set('0')

def delete():
	global expression
	expression=expression.rstrip(expression[-1])
	equation.set(expression)

main_frame=Frame(window,bg="#70214f")
button_frame=Frame(window,bg="#70214f")
main_frame.pack()
button_frame.pack(pady=15)

font_entry=('ariel',25,'bold')
font_button=('new times roman',13,'bold')
equation=StringVar()
equation.set('0')

entry_field=Entry(window,textvariable=equation,font=font_entry, justify='left')
entry_field.pack(ipadx=15,ipady=15,pady=20)

button1=Button(button_frame,width=8,height=3,text="1",relief='raised',bg="#f7f728",font=font_button,borderwidth=2,command=lambda: press(1))
button2=Button(button_frame,width=8,height=3,text="2",relief='raised',bg="#f7f728",font=font_button,borderwidth=2,command=lambda: press(2))
button3=Button(button_frame,width=8,height=3,text="3",relief='raised',bg="#f7f728",font=font_button,borderwidth=2,command=lambda: press(3))
plus=Button(button_frame,width=8,height=3,text="+",relief='raised',bg="#f7f728",font=font_button,borderwidth=2,command=lambda: press("+"))
button4=Button(button_frame,width=8,height=3,text="4",relief='raised',bg="#f7f728",font=font_button,borderwidth=2,command=lambda: press(4))
button5=Button(button_frame,width=8,height=3,text="5",relief='raised',bg="#f7f728",font=font_button,borderwidth=2,command=lambda: press(5))
button6=Button(button_frame,width=8,height=3,text="6",relief='raised',bg="#f7f728",font=font_button,borderwidth=2,command=lambda: press(6))
minus=Button(button_frame,width=8,height=3,text="-",relief='raised',bg="#f7f728",font=font_button,borderwidth=2,command=lambda: press('-'))
button7=Button(button_frame,width=8,height=3,text="7",relief='raised',bg="#f7f728",font=font_button,borderwidth=2,command=lambda: press(7))
button8=Button(button_frame,width=8,height=3,text="8",relief='raised',bg="#f7f728",font=font_button,borderwidth=2,command=lambda: press(8))
button9=Button(button_frame,width=8,height=3,text="9",relief='raised',bg="#f7f728",font=font_button,borderwidth=2,command=lambda: press(9))
multiply=Button(button_frame,width=8,height=3,text="x",relief='raised',bg="#f7f728",font=font_button,borderwidth=2,command=lambda: press("x"))
button0=Button(button_frame,width=8,height=3,text="0",relief='raised',bg="#f7f728",font=font_button,borderwidth=2,command=lambda: press(0))
decimal=Button(button_frame,width=8,height=3,text=".",relief='raised',bg="#f7f728",font=font_button,borderwidth=2,command=lambda: press("."))
clear=Button(button_frame,width=8,height=3,text="C",relief='raised',bg="#f7f728",font=font_button,borderwidth=2,command=lambda: clear())
devide=Button(button_frame,width=8,height=3,text="/",relief='raised',bg="#f7f728",font=font_button,borderwidth=2,command=lambda: press('/'))
equal=Button(button_frame,width=8,height=3,text="=",relief='raised',bg="#f7f728",font=font_button,borderwidth=2,command=lambda: result())
backspace=Button(button_frame,width=8,height=3,text="<<",relief='raised',bg="#f7f728",font=font_button,borderwidth=2,command=lambda: delete())

button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)
plus.grid(row=0,column=3)

button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)
minus.grid(row=1,column=3)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
multiply.grid(row=2,column=3)

button0.grid(row=3,column=0)
decimal.grid(row=3,column=1)
clear.grid(row=3,column=2)
devide.grid(row=3,column=3)

equal.grid(row=4,column=0,columnspan=3,sticky='nsew')
backspace.grid(row=4,column=3)


window.mainloop()