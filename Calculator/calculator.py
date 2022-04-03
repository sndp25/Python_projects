import tkinter.messagebox as m
def add():
    print(int(fentry.get()) + int(sentry.get()))
    m.showinfo('RESULT',f"{fentry.get()} + {sentry.get()} = {int(fentry.get()) + int(sentry.get())}")
def sub():
    print(int(fentry.get()) - int(sentry.get()))
    m.showinfo('RESULT', f"{fentry.get()} - {sentry.get()} = {int(fentry.get()) - int(sentry.get())}")
def mul():
    print(int(fentry.get()) * int(sentry.get()))
    m.showinfo('RESULT', f"{fentry.get()} x {sentry.get()} = {int(fentry.get()) * int(sentry.get())}")
def div():
    print(int(fentry.get()) / int(sentry.get()))
    m.showinfo('RESULT', f"{fentry.get()} `/. {sentry.get()} = {int(fentry.get()) / int(sentry.get())}")
from  tkinter import *
root = Tk()
root.geometry('270x240')
root.title('CALCULATOR')

l1=Label(root,text='FIRST NUMBER',padx=81)
l1.grid()
fvalue=IntVar
fentry=Entry(root,textvariable=fvalue,borderwidth=6,relief=SUNKEN)
fentry.grid()

l2=Label(root,text='SECOND NUMBER')
l2.grid()
svalue=IntVar
sentry=Entry(root,textvariable=svalue,borderwidth=6,relief=SUNKEN)
sentry.grid()

b1=Button(root,text='ADD',command=add,padx=24)
b1.grid()
b2=Button(root,text='SUB ',command=sub,padx=24)
b2.grid()
b3=Button(root,text='MUL ',command=mul,padx=22)
b3.grid()
b4=Button(root,text='DIV',command=div,padx=27)
b4.grid()
root.mainloop()