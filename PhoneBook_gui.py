
#Python Ver: 3.7.1
#
#Author: Matt Kunnari
#
#Purpose: Phonebook Demo, demonstrating OOP, Tkinter GUI, Parent Child Relationships, Sqlite3
#
#
#Tested OS: Code tested to work on Windows 10
#Written: 7/12/2019
import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False,height=False)
        self.master.geometry('{}x{}'.format(700,420))
        self.master.title('Phone Book Application')
        self.master.config(bg='black')

        self.varFName = StringVar()
        self.varLName = StringVar()
        self.varPhone = StringVar()
        self.varEmail = StringVar()

        self.lablFName = Label(self.master,text='First Name:',font=('Helvetica',12),fg='white',bg='black')
        self.lablFName.grid(row=0,column=0,padx=(15,0),pady=(10,0),sticky=NW)
        self.lablLName = Label(self.master,text='Last Name:',font=('Helvetica',12),fg='white',bg='black')
        self.lablLName.grid(row=2,column=0,padx=(15,0),pady=(10,0),sticky=NW)
        self.lablPhone = Label(self.master,text='Phone Number:',font=('Helvetica',12),fg='white',bg='black')
        self.lablPhone.grid(row=4,column=0,padx=(15,0),pady=(10,0),sticky=NW)
        self.lablEmail = Label(self.master,text='E-mail Address:',font=('Helvetica',12),fg='white',bg='black')
        self.lablEmail.grid(row=6,column=0,padx=(15,0),pady=(10,0),sticky=NW)
        self.lablinfoBox = Label(self.master,text='Information:',font=('Helvetica',12),fg='white',bg='black')
        self.lablinfoBox.grid(row=0,column=2,padx=(45,0),pady=(10,0),sticky=NW)

        self.txtBoxFName = Entry(self.master,text=self.varFName,font=('Helvetica',16),fg='black',bg='white')
        self.txtBoxFName.grid(row=1,column=0,columnspan=2,padx=(15,0),pady=(10,0),sticky=NW)
        self.txtBoxLName = Entry(self.master,text=self.varFName,font=('Helvetica',16),fg='black',bg='white')
        self.txtBoxLName.grid(row=3,column=0,columnspan=2,padx=(15,0),pady=(10,0),sticky=NW)
        self.txtBoxAddress = Entry(self.master,text=self.varFName,font=('Helvetica',16),fg='black',bg='white')
        self.txtBoxAddress.grid(row=5,column=0,columnspan=2,padx=(15,0),pady=(10,0),sticky=NW)
        self.txtBoxEmail = Entry(self.master,text=self.varFName,font=('Helvetica',16),fg='black',bg='white')
        self.txtBoxEmail.grid(row=7,column=0,columnspan=2,padx=(15,0),pady=(10,0),sticky=NW)

        self.infoBox = Entry(self.master,text=self.varFName,font=('Helvetica',16),fg='black',bg='white')
        self.infoBox.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(40,0),pady=(10,0),sticky=W+E+N+S)

        self.btnAdd = Button(self.master,text='Add',font=('Helvetica',14),width=10,height=2,fg='black',bg='white')
        self.btnAdd.grid(row=8,column=0,padx=(15,0),pady=(50,0),sticky=NW)
        self.btnUpdate = Button(self.master,text='Update',font=('Helvetica',14),width=10,height=2,fg='black',bg='white')
        self.btnUpdate.grid(row=8,column=1,padx=(20,0),pady=(50,0),sticky=NW)
        self.btnDelete = Button(self.master,text='Delete',font=('Helvetica',14),width=10,height=2,fg='black',bg='white')
        self.btnDelete.grid(row=8,column=2,padx=(20,0),pady=(50,0),sticky=NW)
        self.btnClose = Button(self.master,text='Close',font=('Helvetica',14),width=10,height=2,fg='black',bg='white')
        self.btnClose.grid(row=8,column=4,padx=(90,0),pady=(50,0),sticky=NW)
        







if __name__=="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
