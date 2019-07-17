
import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(441,220))
        self.master.title('Check Files')
        self.master.config(bg='#F0F0F0')

        self.varBrowse1 = StringVar()
        self.varBrowse2 = StringVar()
        
        self.btnBrowse1 = Button(self.master,text='Browse...',width=12,height=1,font=('San Serif',12),fg='black',bg='white')
        self.btnBrowse1.grid(row=0,column=0,padx=(30,0),pady=(50,0),sticky=NW)

        self.btnBrowse2 = Button(self.master,text='Browse...',width=12,height=1,font=('San Serif',12),fg='black',bg='white')
        self.btnBrowse2.grid(row=1,column=0,padx=(30,0),pady=(20,0),sticky=NW)

        self.btnCheck = Button(self.master,text='Check for Files...',width=12,height=2,font=('San Serif',12),fg='black',bg='white')
        self.btnCheck.grid(row=2,column=0,padx=(30,0),pady=(20,0),sticky=NW)

        self.btnClose = Button(self.master,text='Close Program',width=12,height=2,font=('San Serif',12),fg='black',bg='white')
        self.btnClose.grid(row=2,column=3,padx=(0,0),pady=(20,0),sticky=NE)

        self.txtBoxBrowse1 = Entry(self.master,text=self.varBrowse1,font=('San Serif',14),fg='black',bg='white')
        self.txtBoxBrowse1.grid(row=0,column=1,columnspan=3,padx=(45,0),pady=(50,0),sticky=NW)

        self.txtBoxBrowse2 = Entry(self.master,text=self.varBrowse1,font=('San Serif',14),fg='black',bg='white')
        self.txtBoxBrowse2.grid(row=1,column=1,columnspan=3,padx=(45,0),pady=(20,0),sticky=NW)
        





if __name__=="__main__":
    root = Tk()
    App = ParentWindow(root)
    roo.mainloop()
    
