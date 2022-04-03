import tkinter.messagebox as tm
from tkinter import *

def login_window():
   root = Tk()
   root.title('LOGIN')
   root.winfo_geometry
   root.configure(bg='#1C1918')
   textfr=Frame(root,borderwidth=6,relief=SUNKEN,pady=20,padx=20,bg='#fcfcec')
   textfr.grid(padx=10,pady=10)
   wel_fr=Frame(textfr,borderwidth=4,relief=SUNKEN,pady=5,padx=20)
   wel_fr.grid(pady=15)
   Label(wel_fr,text='WELCOME',font=('ARIEL 15 bold')).grid()
   Label(textfr, text='USERNAME').grid()

   uservalue = StringVar()
   userentry = Entry(textfr , textvariable=uservalue)
   userentry.grid()

   Label(textfr , text='PASSWORD').grid()
   bullet = "\u2022" 
   pasvalue = StringVar()
   pasentry = Entry(textfr ,show=bullet, textvariable=pasvalue)
   pasentry.grid()
   def save():
      print(userentry.get(),pasentry.get())
      tm.showinfo('LOGIN','LOGIN SUCCESFULL')
   Button(root, text='LOGIN', command=save).grid()
   root.mainloop()
login_window()