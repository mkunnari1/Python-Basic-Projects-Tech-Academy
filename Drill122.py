
import os
import tkinter as tk
from tkinter import *
import tkinter.filedialog

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)


        self.master = master
        self.master.resizable(width=False,height=False)
        self.master.geometry('{}x{}'.format(600,80))
        self.master.title('Choose Directory')
        self.master.config(bg='#F0F0F0')


        self.lablSelecDir=Label(self.master,text="Selected Directory:",font=('Sans Serif',12),height=1,fg='black',bg='white')
        self.lablSelecDir.grid(row=0,column=1,padx=(15,0),pady=(33,20),sticky=NW)

        self.btnSelecDir=Button(self.master,text="Choose Directory",font=('Sans Serif',12),width=15,fg='black',bg='white',command=self.selectDirect)
        self.btnSelecDir.grid(row=0,column=0,padx=(20,0),pady=(30,20),sticky=NW)

        self.lablDir=Label(self.master,text='',font=('Sans Serif',12),fg='black',bg='#F0F0F0')
        self.lablDir.grid(row=0,column=2,columnspan=3,padx=(15,0),pady=(33,20),sticky=NW)

    def selectDirect(self):
        
        print('initialize selectDirect')
        dirname = tkinter.filedialog.askdirectory()
        print(dirname)
        self.lablDir.config(text="{}".format(dirname),bg='white')
        
        
        







if __name__=="__main__":
    root = Tk()
    App=ParentWindow(root)
    root.mainloop()
    
