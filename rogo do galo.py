from tkinter import *

jdg = Tk()
jdg.title('Jogo do Galo')
q1 = 1
q2 = 2
q3 = 3
q4 = 4
q5 = 5
q6 = 6
q7 = 7
q8 = 8
q9 = 9
def ganho():
    label.config(text="Ganhaste")

def xouo1():
    q1 = 10
def xouo2():
    q2 = 10
def xouo3():
    q3 = 10
def xouo4():
    q4 = 10
def xouo5():
    q5 = 10
def xouo6():
    q6 = 10
def xouo7():
    q7 = 10
def xouo8():
    q8 = 10
def xouo9():
    q9 = 10
b1= Button(jdg,text='---',width=10, height=5,command=xouo1).grid(column=0,row=0)
b2 = Button(jdg,text='---',width=10, height=5,command=xouo2).grid(column=1,row=0)
b3 = Button(jdg,text='---',width=10, height=5,command=xouo3).grid(column=2,row=0)
b4 = Button(jdg,text='---',width=10, height=5,command=xouo4).grid(column=0,row=1)
b5 = Button(jdg,text='---',width=10, height=5,command=xouo5).grid(column=1,row=1)
b6 = Button(jdg,text='---',width=10, height=5,command=xouo6).grid(column=2,row=1)
b7 = Button(jdg,text='---',width=10, height=5,command=xouo7).grid(column=0,row=2)
b8 = Button(jdg,text='---',width=10, height=5,command=xouo8).grid(column=1,row=2)
b9 = Button(jdg,text='---',width=10, height=5,command=xouo9).grid(column=2,row=2)
lbl = Label(text='',width=10,height=5).grid(column=1,row=3)
if q1 == q2 == q3:
    ganho()
    print('ganhaste')
elif q4 == q5 == q6:
    ganho()
    print('ganhaste')
elif q7 == q8 == q9:
    ganho()
    print('ganhaste')
elif q1 == q5 == q9:
    ganho()
    print('ganhaste')
elif q3 == q5 == q9:
    ganho()
    print('ganhaste')
elif q1 == q4 == q7:
    ganho()
    print('ganhaste')
elif q2 == q5 == q8:
    ganho()
    print('ganhaste')
elif q3 == q6 == q9:
    ganho()
    print('ganhaste')
jdg.mainloop()
