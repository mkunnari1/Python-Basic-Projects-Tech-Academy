

import tkinter as tk
import os
import sqlite3
import shutil
from sqlite3 import *
from shutil import *
from os import *
from tkinter import *
import tkinter.filedialog

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True,height=False)
        self.master.geometry('{}x{}'.format(1000,280))
        self.master.minsize(600,200)
        self.master.title('.txt File Transfer')
        self.master.config(bg='#F0F0F0')

        self.lablSelecDir=Label(self.master,text="Source Directory:",font=('Sans Serif',12),height=1,fg='black',bg='white')
        self.lablSelecDir.grid(row=0,column=1,padx=(15,0),pady=(40,0),sticky=NW)
        
        self.lablSelecDir=Label(self.master,text="Destination Directory:",font=('Sans Serif',12),height=1,fg='black',bg='white')
        self.lablSelecDir.grid(row=1,column=1,padx=(15,0),pady=(15,0),sticky=NW)
        
        self.lablDir1=Label(self.master,text='',font=('Sans Serif',12),fg='black',bg='#F0F0F0')
        self.lablDir1.grid(row=0,column=2,columnspan=3,padx=(15,0),pady=(40,20),sticky=NW)

        self.lablDir2=Label(self.master,text='',font=('Sans Serif',12),fg='black',bg='#F0F0F0')
        self.lablDir2.grid(row=1,column=2,columnspan=3,padx=(15,0),pady=(15,20),sticky=NW)

        self.btnSelecDir1=Button(self.master,text="Browse Directory",font=('Sans Serif',12),width=15,fg='black',bg='white',command=self.selectDirect1)
        self.btnSelecDir1.grid(row=0,column=0,padx=(20,0),pady=(40,20),sticky=NW)

        self.btnSelecDir2=Button(self.master,text="Browse Directory",font=('Sans Serif',12),width=15,fg='black',bg='white',command=self.selectDirect2)
        self.btnSelecDir2.grid(row=1,column=0,padx=(20,0),pady=(15,20),sticky=NW)

        self.btnFileTransfer=Button(self.master,text='Initiate File Transfer',font=('Sans Serif',12),width=20,height=2,fg='black',bg='white',command=self.initTrans)
        self.btnFileTransfer.grid(row=2,column=0,padx=(80,0),pady=(20,0),sticky=NW)
        
        self.btnFileTransfer=Button(self.master,text='Cancel',font=('Sans Serif',12),width=20,height=2,fg='black',bg='white',command=self.cancel)
        self.btnFileTransfer.grid(row=2,column=1,padx=(40,0),pady=(20,0),sticky=NW)
        


    def selectDirect1(self):
        
        print('initialize selectDirect')
        dirname = tk.filedialog.askdirectory()
        print(dirname)
        self.lablDir1.config(text="{}".format(dirname),bg='white')

    def selectDirect2(self):
        
        print('initialize selectDirect')
        dirname = tk.filedialog.askdirectory()
        print(dirname)
        self.lablDir2.config(text="{}".format(dirname),bg='white')

    def cancel(self):
        print('init destroy')
        self.master.destroy()

    def initTrans(self):
        print('init Transfer')

        def conn(self):
            dbconn=sqlite3.connect('drill123.db')

            with dbconn:
                cur = dbconn.cursor()
                cur.execute('create table if not exists tbl_files(col_Filename string,col_fileTime string)')

                dbconn.commit()
            dbconn.close()

        conn(self)

        def getFiles(self):


            listDir=os.listdir('{}'.format(self.lablDir1.cget('text')))

            fpath='{}'.format(self.lablDir1.cget('text'))

            destination = '{}'.format(self.lablDir2.cget('text'))


            for file in listDir:
                if file.endswith('.txt'):

                    fullFile=os.path.join(fpath,file)
                    fileTime=str(os.path.getmtime(fullFile))
                    
                    print(fullFile+fileTime+' initiate transfer, uploading to DB')
                    shutil.copy(fullFile,destination)

                    dbconn = sqlite3.connect('drill123.db')

                    with dbconn:
                        cur=dbconn.cursor()
                        cur.execute('insert into tbl_files values(?,?)',(fullFile,fileTime))
                        dbconn.commit()
                    dbconn.close()

                    print('getFiles complete')

        getFiles(self)
        

                    
        






if __name__=="__main__":
    root = Tk()
    App=ParentWindow(root)
    root.mainloop()
    
