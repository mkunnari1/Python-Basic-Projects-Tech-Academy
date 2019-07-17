
import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('Learning Tkinter')
        self.master.config(bg='#ED7EFF')

        self.varFName = StringVar()
        self.varLName = StringVar()

        self.lablFName = Label(self.master,text='First Name',font=('Helvetica', 14), fg='lightblue',bg='black')
        self.lablFName.grid(row=0,column=0,padx=(10,0),pady=(20,0))
        self.lablLName = Label(self.master,text='Last Name',font=('Helvetica', 14), fg='lightblue',bg='black')
        self.lablLName.grid(row=1,column=0,padx=(10,0),pady=(20,0))

        self.lablDisplay = Label(self.master,text='',font=('Helvetica', 14), fg='Green',bg='#ED7EFF')
        self.lablDisplay.grid(row = 3, column = 1,padx=(10,0),pady=(20,0))
        
        self.txtBoxFName = Entry(self.master,text = self.varFName, font = ('Helvetica', 16), fg='black', bg='lightblue')
        self.txtBoxFName.grid(row = 0, column = 1,padx=(10,0),pady=(20,0))

        self.txtBoxLName = Entry(self.master,text = self.varLName, font = ('Helvetica', 16), fg='black', bg='lightblue')
        self.txtBoxLName.grid(row =1 , column =1,padx=(10,0),pady=(20,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10,height=2,font = ('Helvetica',12),fg='lightgray',bg='purple',command=self.submit)
        self.btnSubmit.grid(row=2,column=1,padx=(0,0),pady=(20,0),sticky=NE)

        self.btnClose = Button(self.master, text="Close",width=10,height=2,font=('Helvetica',12),fg='black',bg='orange',command=self.cancel)
        self.btnClose.grid(row=2,column=1,padx=(10,0),pady=(20,0),sticky=NW)

    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lablDisplay.config(text="Hello {} {}!".format(fn,ln))
    def cancel(self):
        self.master.destroy()
        
        

        


        



if __name__=="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
