
#Python Ver: 3.7.1
#
#Author: Matt Kunnari
#
#Purpose: Phonebook Demo, demonstrating OOP, Tkinter GUI, Parent Child Relationships, Sqlite3
#
#
#Tested OS: Code tested to work on Windows 10
#Written: 7/12/2019

from tkinter import *
import tkinter as tk

#load all our other modules as well

import phonebook_main_matt
import phonebook_func_matt

def load_gui(self):

    self.labl_fname = tk.Label(self.master,text='First Name:')
    self.labl_fname.grid(row=0,column=o,padx=(27,0),pady(10,0),sticky=NW)
    self.labl_lname = tk.Label(self.master,text='Last Name:')
    self.labl_lname.grid(row=2,column=o,padx=(27,0),pady(10,0),sticky=NW)
    self.labl_phone = tk.Label(self.master,text='Phone Number:')
    self.labl_phone.grid(row=4,column=o,padx=(27,0),pady(10,0),sticky=NW)
    self.labl_email = tk.Label(self.master,text='E-mail Address:')
    self.labl_email.grid(row=6,column=o,padx=(27,0),pady(10,0),sticky=NW)
    self.labl_user = tk.Label(self.master,text='User:')
    self.labl_user.grid(row=0,column=2,padx=(0,0),pady(10,0),sticky=NW)

    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),stikcy=N+E+W)
    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),stikcy=N+E+W)
    self.txt_phone = tk.Entry(self.master,text='')
    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),stikcy=N+E+W)
    self.txt_email = tk.Entry(self.master,text='')
    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),stikcy=N+E+W)

    #this is the list box with scrollbar
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.1stlist1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
    self.1stlist1.bind('<<ListboxSelect>>',lambda event: phonebook_func_matt.onSelect(self,event))
    self.scrollbar1.config(command=self.1stlist1.yview)
    self.scrollbar1.grid(row=1,column=5,rowspan=7,coumnspan=1,padx=(0,0),pady(0,0),sticky=N+E+S)
    self.1stlist1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady(0,0),sticky=N+E+S+W)

    self.btn_add = tk.Button(self.master,width=12,height=2,text='Add',command=lambda:phonebook_func_matt.addToList(self))
    self.btn_add.grid(row=8,column=0,padx=(25,0),pady=(45,10),stikcy=W)
    self.btn_update = tk.Button(self.master,width=12,height=2,text='Add',command=lambda:phonebook_func_matt.onUpdate(self))
    self.btn_update.grid(row=8,column=1,padx=(25,0),pady=(45,10),stikcy=W)
    self.btn_delete = tk.Button(self.master,width=12,height=2,text='Add',command=lambda:phonebook_func_matt.onDelete(self))
    self.btn_delete.grid(row=8,column=2,padx=(25,0),pady=(45,10),stikcy=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Add',command=lambda:phonebook_func_matt.ask_quit(self))
    self.btn_close.grid(row=8,column=4,padx=(25,0),pady=(45,10),stikcy=E)

    
    phonebook_func_matt.create_db(self)
    phonebook_func_matt.onRefresh(self)



if __name__=="__main__":
   pass
